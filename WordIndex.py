# WordIndex.py
# Name:
# Date:
# Assignment:

def main():
    file_name = input(" Enter a file name:")
    try:
        with open(file_name, 'r') as textFile:
            words = {}  # Dictionary to store words and their line numbers
            for line_number, line in enumerate(textFile, start=1):
                for word in line.strip().split():
                    word = word.lower().strip('.,!?"()')  # Normalize word
                    if word in words:
                        words[word].append(line_number)
                    else:
                        words[word] = [line_number]

            for word in sorted(words):
                print(f"{word}: {words[word]}")
    except FileNotFoundError:
        print("File not found.")

if __name__ == "__main__":
    main()