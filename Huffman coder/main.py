from huffman import Huffman


def main():
    inputPath = "Huffman coder/data/poem.txt"
    outputPath = "Huffman coder/data/poem.huff"
    freqsPath = "Huffman coder/data/freqs.huff"

    # Reading a file
    with open(inputPath, "r", encoding="utf-8") as f:
        text = f.read().rstrip()

    # Calculate the initial text size
    S = len(text.encode("utf-8")) * 8
    print(f"The length |S| of the source text in bits = {S}")

    # Huffman coder usage
    huff = Huffman()
    root = huff.buildHuffmanTree(text)
    huffmanCodes = huff.buildHuffmanCodes(root)
    encodedText = huff.encodeText(text, huffmanCodes)

    # Calculate the encoded text size
    C = len(encodedText)
    print(f"The length |C| of the encoded text in bits = {C}")
    print(f"Compression ratio k = |S|/|C| = {S/C}")

    freqs = {key: freq / len(text) for key, freq in huff.frequency.items()}

    # Writing the frequency of characters
    with open(freqsPath, "w", encoding="utf-8") as f:
        sortedFreqs = sorted(freqs.items(), key=lambda x: x[1], reverse=True)
        for char, freq in sortedFreqs:
            f.write(f"{char}:{freq}\n")

    # Writing encoded poem to a file
    with open(outputPath, "w", encoding="utf-8") as f:
        sorted_codes = sorted(
            huffmanCodes.items(), key=lambda item: huff.frequency[item[0]], reverse=True
        )
        for char, code in sorted_codes:
            f.write(f"{char}:{code}\n")
        f.write("\n" + encodedText)


if __name__ == "__main__":
    main()
