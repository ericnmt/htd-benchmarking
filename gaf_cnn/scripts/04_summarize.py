import numpy as np
from collections import defaultdict

# Read results/results.txt. If a (dataset, method, seed) was logged more than once,
# the LAST line wins.
runs = {}
with open("results/results.txt") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        parts = [p.strip() for p in line.split("|")]
        data, rest = parts[0], dict(p.split("=", 1) for p in parts[1:-1])
        # the last field looks like "acc=0.9982 f1=0.9982 auc=1.0000"
        tail = dict(kv.split("=") for kv in parts[-1].split())
        key = (data, rest["method"], int(rest["seed"]))
        runs[key] = {k: float(tail[k]) for k in ("acc", "f1", "auc")}

by_group = defaultdict(dict)   # (data, method) -> {seed: metrics}
for (data, method, seed), m in runs.items():
    by_group[(data, method)][seed] = m

for (data, method), seeds in sorted(by_group.items()):
    accs = np.array([m["acc"] for m in seeds.values()])
    f1s = np.array([m["f1"] for m in seeds.values()])
    aucs = np.array([m["auc"] for m in seeds.values()])
    sd = lambda a: a.std(ddof=1) if len(a) > 1 else float("nan")
    print(f"{data:8s} {method:7s} n={len(accs)}  "
          f"acc={accs.mean():.4f} +/- {sd(accs):.4f}  "
          f"(min {accs.min():.4f}, max {accs.max():.4f})  "
          f"f1={f1s.mean():.4f}  auc={aucs.mean():.4f}")

# paired comparison: same seed means same train/test split for both methods
for data in sorted({d for d, _ in by_group}):
    a, b = by_group.get((data, "avg"), {}), by_group.get((data, "interp"), {})
    shared = sorted(set(a) & set(b))
    if shared:
        diffs = np.array([a[s]["acc"] - b[s]["acc"] for s in shared])
        print(f"\n{data} paired (avg - interp) accuracy by seed:")
        for s, d in zip(shared, diffs):
            print(f"  seed {s}: {d:+.4f}")
        sd = diffs.std(ddof=1) if len(diffs) > 1 else float("nan")
        print(f"  mean diff {diffs.mean():+.4f}, std {sd:.4f}, "
              f"avg better in {(diffs > 0).sum()}/{len(diffs)} seeds, "
              f"tied in {(diffs == 0).sum()}")