import numpy as np


def sampleEntropy(signal, m, r):
    # Count the number of similar patterns of length m in the signal within a given tolerance r
    def _phi(m):
        N = len(signal)
        templates = np.array([signal[i : i + m] for i in range(N - m + 1)])
        count = 0
        # Correlation integral
        for i in range(len(templates)):
            # Chebyshev distance
            dist = np.max(np.abs(templates - templates[i]), axis=1)
            # We exclude the coincidence of the template with itself (subtracting 1)
            count += np.sum(dist <= r) - 1
        return count / (len(templates) * (len(templates) - 1))

    B = _phi(m)
    A = _phi(m + 1)

    return -np.log(A / B) if B > 0 else float("inf")
