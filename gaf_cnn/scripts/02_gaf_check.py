import numpy as np
import matplotlib.pyplot as plt
from htd_benchmarking.gaf import make_images

d = np.load("data/processed/AES-T800+TrojanDisabled_2.npy")[:1]
t = np.load("data/processed/AES-T800+TrojanTriggered_2.npy")[:1]
di, ti = make_images(d)[0], make_images(t)[0]

fig, ax = plt.subplots(2, 2, figsize=(8, 8))
for r, (img, name) in enumerate([(di, "Disabled"), (ti, "Triggered")]):
    for c, label in enumerate(["GASF", "raw reshaped"]):
        ax[r, c].imshow(img[c], cmap="viridis")
        ax[r, c].set_title(f"{name} - {label}")
plt.savefig("results/figures/gaf_check.png")
print("saved")