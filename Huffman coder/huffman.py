import heapq
from collections import Counter
from shannon import shannonEntropy


class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


class Huffman:
    def buildHuffmanTree(self, text):
        self.frequency = Counter(text)
        
        print(f"Shannon entropy = {shannonEntropy(text)}")
        
        priority_queue = [HuffmanNode(char, freq) for char, freq in self.frequency.items()]
        heapq.heapify(priority_queue)

        while len(priority_queue) > 1:
            left = heapq.heappop(priority_queue)
            right = heapq.heappop(priority_queue)
            merged = HuffmanNode(None, left.freq + right.freq)
            merged.left = left
            merged.right = right
            heapq.heappush(priority_queue, merged)

        return priority_queue[0] if priority_queue else None

    def buildHuffmanCodes(self, root):
        codes = {}

        def dfs(node, code):
            if node is not None:
                if node.char is not None:
                    codes[node.char] = code
                dfs(node.left, code + "0")
                dfs(node.right, code + "1")

        dfs(root, "")
        return codes

    def encodeText(self, text, codes):
        return "".join(codes[char] for char in text)
