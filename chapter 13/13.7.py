file = open("hangman.txt", "r").read()
words = [word for word in file.split()]
print(words)