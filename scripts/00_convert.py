import numpy as np
import os
import sys
import time

""" Data preparation step.
# Convert raw data into numpy arrays.
# How to use:
    - Enter root path of uncompressed data into the SRC variable
    - Enter the path to the destination for the numpy array (revise)
"""

SRC = os.path.expanduser("~/Documents/trojan-dataset/uncompressed/AES-T800_power_Temp25C")
DEST = os.path.expanduser("~/Repositories/htd-benchmarking/data/processed")
N_TRACES, N_SAMPLES = 10_000, 2_500

def convert(cond):
    """Convert raw traces to numpy arrays."""
    inner = os.path.join(SRC, cond, cond)
    X = np.empty((N_TRACES, N_SAMPLES), dtype=np.float32)
    for i in range(N_TRACES):
        with open(os.path.join(inner, f"Sample_{i}.csv")) as fh:
            row = np.array(fh.read().split(), dtype=np.float32)
        assert row.shape == (N_SAMPLES,), f"{cond}/Sample_{i}.csv has {row.shape}"
        X[i] = row
    np.save(os.path.join(DEST, f"{cond}.npy"), X)

    return X

# Convert Disabled and Triggered data for both types (1 and 2)
convert("AES-T800+TrojanDisabled_1")
convert("AES-T800+TrojanDisabled_2")
convert("AES-T800+TrojanTriggered_1")
convert("AES-T800+TrojanTriggered_2")

