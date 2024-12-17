import numpy as np


def sample_entropy(signal, m, r):
    def _phi(m):
        N = len(signal)
        templates = np.array([signal[i : i + m] for i in range(N - m + 1)])
        count = 0
        for i in range(len(templates)):
            dist = np.max(np.abs(templates - templates[i]), axis=1)
            count += np.sum(dist <= r) - 1
        return count / (len(templates) * (len(templates) - 1))

    B = _phi(m)
    A = _phi(m + 1)

    return -np.log(A / B) if B > 0 else float("inf")
