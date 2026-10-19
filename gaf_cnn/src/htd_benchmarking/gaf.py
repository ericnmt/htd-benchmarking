import numpy as np

def resample_interp(X, n):
    """Point-sample each row of X (N, L) at n evenly spaced positions (linear interpolation).
    No averaging, so narrow spikes can be missed or caught depending on alignment."""
    old = np.linspace(0, 1, X.shape[1])
    new = np.linspace(0, 1, n)
    return np.stack([np.interp(new, old, row) for row in X]).astype(np.float32)

def resample_avg(X, n):
    """Average each row of X (N, L) into n near-equal bins (aggregation downsampling)."""
    edges = np.linspace(0, X.shape[1], n + 1).astype(int)
    return np.stack([X[:, a:b].mean(axis=1)
                     for a, b in zip(edges[:-1], edges[1:])], axis=1).astype(np.float32)

def minmax(X):
    """Scale each row to [-1, 1]."""
    lo = X.min(axis=1, keepdims=True)
    hi = X.max(axis=1, keepdims=True)
    return (2 * (X - lo) / (hi - lo + 1e-8) - 1).astype(np.float32)

def gasf(X):
    """(N, n) in [-1, 1] -> (N, n, n) via cos(theta_i + theta_j)."""
    phi = np.arccos(np.clip(X, -1, 1))
    return np.cos(phi[:, :, None] + phi[:, None, :]).astype(np.float32)

def make_images(X, method="avg"):
    """(N, 2500) raw traces -> (N, 2, 64, 64): [GASF, reshaped raw].

    method="avg"    : channel 1 built from a block-averaged 64-sample trace
    method="interp" : channel 1 built from a point-sampled 64-sample trace (v1 behavior)
    Channel 2 (raw signal reshaped to 64x64) always uses interpolation, since it
    upsamples 2500 -> 4096 samples.
    """
    if method == "avg":
        small = resample_avg(X, 64)
    elif method == "interp":
        small = resample_interp(X, 64)
    else:
        raise ValueError(f"unknown method: {method!r} (use 'avg' or 'interp')")
    ch1 = gasf(minmax(small))
    ch2 = minmax(resample_interp(X, 4096)).reshape(-1, 64, 64)
    return np.stack([ch1, ch2], axis=1)