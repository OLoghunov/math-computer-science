from huffman import Huffman


def main():
    inputPath = "Huffman coder/data/poem.txt"
    outputPath = "Huffman coder/data/encodedPoem.txt"

    with open(inputPath, 'r', encoding='utf-8') as f:
        text = f.read()
        text = text.rstrip()

    huff = Huffman()

    root = huff.build_huffman_tree(text)
    huffmanCodes = huff.build_huffman_codes(root)
    encodedText = huff.encode_text(text, huffmanCodes)

    with open(outputPath, "w", encoding='utf-8') as f:
        sorted_codes = sorted(huffmanCodes.items(), key=lambda item: huff.frequency[item[0]], reverse=True)
        for char, code in sorted_codes:
            f.write(f"{char}:{code}\n")
        f.write("\n" + encodedText)


if __name__ == "__main__":
    main()
