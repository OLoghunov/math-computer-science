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
    epsRange = np.arange(0.1, 1.1, 0.005)
    m = 2

    entropies = np.zeros(shape=(3, len(epsRange)))

    for i, path in enumerate(paths):

        # We read every fifth entry
        data = pd.read_excel(
            path, header=None, usecols=[2], skiprows=lambda x: x % 5 != 0
        ).to_numpy()

        xrange = []
        
        start_time = time.time()

        for j, eps in enumerate(epsRange):
            entropy = sampleEntropy(data, m, eps)
            entropies[i][j] = entropy
            xrange.append(eps)

        print("--- %s seconds ---" % (time.time() - start_time))

    view(entropies, xrange)


if __name__ == "__main__":
    print("Entropy estimation")
    main()
