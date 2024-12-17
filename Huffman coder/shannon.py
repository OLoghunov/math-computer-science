from collections import Counter
import math


def shannonEntropy(text):
    frequency = Counter(text)
    pk = [freq / len(text) for freq in frequency.values()]
    entropy = 0
    for p in pk:
        if p > 0:  # the range of acceptable values for the logarithm
            entropy -= p * math.log(p, 2)

    return entropy
