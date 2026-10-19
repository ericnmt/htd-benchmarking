import numpy as np
import matplotlib.pyplot as plt

DATA_DIR = "data/processed"

x = np.load(f"{DATA_DIR}/AES-T800+TrojanDisabled_2.npy")
y = np.load(f"{DATA_DIR}/AES-T800+TrojanTriggered_2.npy")

print("shape:", x.shape)
print("dtype:", x.dtype)
print("first trace, first 10 values:", x[0, :10])
print("mean of whole array:", x.mean())


plt.plot(x[0], label="Disabled")
plt.plot(y[0], label="Triggered")
plt.title("Disabled vs Triggered Trace comparison")
plt.xlabel("Sample index")
plt.ylabel("power (raw units)")
plt.legend()
plt.savefig("results/figures/dill_trace.png")
print("saved plot")

disabled_mean = x.mean(axis=0)
triggered_mean = y.mean(axis=0)

plt.figure()
plt.plot(disabled_mean, label="Disabled mean")
plt.plot(triggered_mean, label="Triggered mean")
plt.title("Mean Trace comparison")
plt.xlabel("Sample index")
plt.ylabel("power (raw units)")
plt.legend()
plt.savefig("results/figures/dill_mean_trace.png")
print("saved mean comparison plot")

diff = triggered_mean - disabled_mean

plt.figure()
plt.plot(diff)
plt.axhline(0, color="gray", linewidth=0.5)
plt.title("Difference between Triggered and Disabled mean traces")
plt.xlabel("Sample index")
plt.ylabel("power (raw units)")
plt.savefig("results/figures/dill_mean_diff.png")
print("saved mean difference plot")