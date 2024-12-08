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

    epsRange = np.arange(0.1, 1.1, 0.005)
    nrows = len(epsRange)

    entropies = np.zeros(shape=(3, nrows))
    d = 2

    for i, path in enumerate(paths):
        data = pd.read_excel(path, header=None, nrows=200).iloc[:, [2]].to_numpy()

        # O(n^2 * d)
        # eps = 0.2 * np.std(data)  # порог (20% стандартного отклонения)

        xrange = []
        start_time = time.time()

        for j, eps in enumerate(epsRange):
            entropy = sample_entropy(data, d, eps)
            entropies[i][j] = entropy
            xrange.append(eps)

        print("--- %s seconds ---" % (time.time() - start_time))

    view(entropies, xrange)


if __name__ == "__main__":
    main()
