
def countLetters(s):
    count = 0
    for i in s:
        if i.isalpha():
            count += 1
    return count

userString = input("Enter a string: ")
print(f"The number of letters in {userString} is {countLetters(userString)}")
