
filename = input("Enter a filename: ")
file = open(filename, "r")
text = file.read()
vowels = {"a", "e", "i", "o", "u"}
vowelsCount = 0
consonantsCount = 0
for letter in text:
    if letter.isalpha():
        if letter.lower() in vowels:
            vowelsCount += 1
        else:
            consonantsCount += 1

print(f"Vowels: {vowelsCount}")
print(f"Consonants: {consonantsCount}")
file.close()
