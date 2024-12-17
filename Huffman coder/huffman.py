import heapq
from collections import Counter


class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # Need to override the < operator for the priority queue
    def __lt__(self, other):
        return self.freq < other.freq


class Huffman:
    def buildHuffmanTree(self, text):
        self.frequency = Counter(text)
        
        # Priority queue helps to build a Huffman tree
        priority_queue = [HuffmanNode(char, freq) for char, freq in self.frequency.items()]
        heapq.heapify(priority_queue)

        # Build a Huffman tree
        while len(priority_queue) > 1:
            
            # We take two nodes with the smallest frequencies
            left = heapq.heappop(priority_queue)
            right = heapq.heappop(priority_queue)
            
            # Merge them into a new node
            merged = HuffmanNode(None, left.freq + right.freq)
            merged.left = left
            merged.right = right
            
            # Add the new node to the priority queue
            heapq.heappush(priority_queue, merged)

        return priority_queue[0] if priority_queue else None

    def buildHuffmanCodes(self, root):
        codes = {}

        # Depth-first search
        def dfs(node, code):
            if node is not None:
                # If the current node is a leaf node
                if node.char is not None:
                    # Add the code to the dictionary
                    codes[node.char] = code
                # Recursively traverse the left and right subtrees
                dfs(node.left, code + "0")
                dfs(node.right, code + "1")

        dfs(root, "")
        return codes

    # Encode the text using the Huffman codes
    def encodeText(self, text, codes):
        return "".join(codes[char] for char in text)
