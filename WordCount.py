# WordCount.py
# Name:
# Date:
# Assignment:

def main():
    file_name = input(" Enter a file name:" )
    try:
        with open(file_name, 'r') as textFile:
            lines = textFile.readlines()
            word_count = sum(len(line.split()) for line in lines)
            char_count = sum(len(line) for line in lines)
            print(f"Lines: {len(lines)}")
            print(f"Words: {word_count}")
            print(f"Characters: {char_count}")
    except FileNotFoundError:
        print("File not found.")

if __name__ == "__main__":
    main()
