from collections import Counter
import math

# The function returns a value between 0 (perfectly predictable) 
# and the logarithm of the number of unique characters (completely random).
def shannonEntropy(text):
    frequency = Counter(text)
    # Calculate the probabilities of each character
    pk = [freq/len(text) for freq in frequency.values()]
    entropy = 0
    for p in pk:
        if p > 0:  # check the range of acceptable values for the logarithm
            entropy -= p * math.log(p, 2)

    return entropy