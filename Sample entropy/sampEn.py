import numpy as np


def sample_entropy(time_series, d, eps):
    n = len(time_series)
    if n <= d + 1:
        raise ValueError("Time series is too short for given d.")

    def _phi(d):
        count = 0
        for i in range(n - d):
            for j in range(i + 1, n - d):
                if (
                    np.max(np.abs(time_series[i : i + d] - time_series[j : j + d]))
                    <= eps
                ):
                    count += 1
        return count

    a = _phi(d)
    b = _phi(d + 1)

    # Avoid log(0) by checking b
    return -np.log(b / a) if b > 0 else np.inf
