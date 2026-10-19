import sys
import numpy as np
import torch, torch.nn as nn
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score, roc_auc_score
from htd_benchmarking.gaf import make_images

# usage: uv run scripts/03_train_cnn.py [avg|interp] [seed]
METHOD = sys.argv[1] if len(sys.argv) > 1 else "avg"
SEED = int(sys.argv[2]) if len(sys.argv) > 2 else 0
if METHOD not in ("avg", "interp"):
    sys.exit(f"unknown method {METHOD!r}: use 'avg' or 'interp'")
torch.manual_seed(SEED)

D = "data/processed"
d = np.load(f"{D}/AES-T800+TrojanDisabled_2.npy")
t = np.load(f"{D}/AES-T800+TrojanTriggered_2.npy")
X = np.concatenate([d, t])
y = np.concatenate([np.zeros(len(d)), np.ones(len(t))]).astype(np.float32)

# split by TRACE, before imaging
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2,
                                      stratify=y, random_state=SEED)
Itr = torch.from_numpy(make_images(Xtr, method=METHOD))
Ite = torch.from_numpy(make_images(Xte, method=METHOD))
ytr, yte = torch.from_numpy(ytr), torch.from_numpy(yte)

def block(i, o):
    return nn.Sequential(nn.Conv2d(i, o, 3, padding=1), nn.ReLU(), nn.MaxPool2d(2))

model = nn.Sequential(block(2, 16), block(16, 32), block(32, 64),
                      nn.Flatten(), nn.Linear(64 * 8 * 8, 64), nn.ReLU(),
                      nn.Linear(64, 1))
opt = torch.optim.Adam(model.parameters(), lr=1e-3)
loss_fn = nn.BCEWithLogitsLoss()

print(f"resampling method: {METHOD}  seed: {SEED}")
for epoch in range(20):
    model.train()
    perm = torch.randperm(len(Itr))
    for i in range(0, len(perm), 128):
        idx = perm[i:i + 128]
        opt.zero_grad()
        loss = loss_fn(model(Itr[idx]).squeeze(1), ytr[idx])
        loss.backward()
        opt.step()
    model.eval()
    with torch.no_grad():
        p = torch.sigmoid(model(Ite).squeeze(1)).numpy()
    acc = accuracy_score(yte, p > 0.5)
    f1 = f1_score(yte, p > 0.5)
    auc = roc_auc_score(yte, p)
    print(f"epoch {epoch+1}: acc={acc:.4f} f1={f1:.4f} auc={auc:.4f}")

# one line per run, so results from different methods can be compared later
with open("results/results.txt", "a") as f:
    f.write(f"T800 _2 | method={METHOD} | seed={SEED} | epoch=20 | "
            f"acc={acc:.4f} f1={f1:.4f} auc={auc:.4f}\n")
print("appended to results/results.txt")