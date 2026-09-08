import numpy as np
import os

"""
Script to verify that the conversion was successful. Checks for the following conditions:
    - shape, should be 10000, 2500
    - NaNs, should be 0 (ensures clean data)
"""

DATA = os.path.expanduser("~/Repositories/htd-benchmarking/data/processed")

for c in ["Disabled_1", "Disabled_2", "Triggered_1", "Triggered_2"]:
    path = f"{DATA}/AES-T800+Trojan{c}.npy"
    X = np.load(path)
    print(f"{c:12s} shape={X.shape} dtype={X.dtype} nan={np.isnan(X).sum()} "
        f"mean={X.mean():.3f} ")

# Print out mean and comparisons.
d1 = np.load(f"{DATA}/AES-T800+TrojanDisabled_1.npy")
t1 = np.load(f"{DATA}/AES-T800+TrojanTriggered_1.npy")
print(f"Disabled_1 mean={d1.mean():.4f}  Triggered_1 mean={t1.mean():.4f}  "
      f"diff={t1.mean()-d1.mean():.4f}")

d2 = np.load(f"{DATA}/AES-T800+TrojanDisabled_2.npy")
t2 = np.load(f"{DATA}/AES-T800+TrojanTriggered_2.npy")
print(f"\nDisabled_2 mean={d2.mean():.4f}  Triggered_2 mean={t2.mean():.4f}  "
      f"diff={t2.mean()-d2.mean():.4f}")