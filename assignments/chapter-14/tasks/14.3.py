import os.path
import sys


def main():
    keyWords = {"and", "as", "assert", "break", "class",
        "continue", "def", "del", "elif", "else",
        "except", "False", "finally", "for", "from",
        "global", "if", "import", "in", "is", "lambda",
        "None", "nonlocal", "not", "or", "pass", "raise",
         "return", "True", "try", "while", "with", "yield"}

    occurences = [0] * len(keyWords)
    print(occurences)

    filename = input("Enter a Python source code filename: ").strip()
    if not os.path.isfile(filename):
        print("File", filename, "does not exist")
        sys.exit()

    infile = open(filename, "r")

    text = infile.read().split()

    for word in text:
        if word in keyWords:
            index = list(keyWords).index(word)
            occurences[index] += 1

    keyWords = list(keyWords)
    for i in range(len(keyWords)):
        print(f"{keyWords[i]}: {occurences[i]}")


main()

