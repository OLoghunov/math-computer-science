import pandas as pd
import numpy as np
import time

from sampEn import *
from view import view

def main():
    paths = [
        "Sample entropy/data/1.xlsx",
        "Sample entropy/data/2.xlsx",
        "Sample entropy/data/3.xlsx",
    ]

    # SampEn parameters
    epsRange = np.arange(0.1, 1.1, 0.05)
    mRange = range(1, 42, 10)

    entropies = np.zeros((3, len(mRange), len(epsRange)))

    for i, path in enumerate(paths):

        # We read every fifth entry 
        data = pd.read_excel(
            path, header=None, nrows=2000, usecols=[2], skiprows=lambda x: x % 5 != 0
        ).to_numpy()

        for k, m in enumerate(mRange):
            start_time = time.time()

            for j, eps in enumerate(epsRange):
                entropy = sampleEntropy(data, m, eps)
                entropies[i, k, j] = entropy

            print(f"File {i+1}.xlsx,\t m={m},\t estimation time: {round(time.time() - start_time, 2)} seconds")

    view(entropies, epsRange, mRange)

if __name__ == "__main__":
    print("Entropy estimation")
    main()