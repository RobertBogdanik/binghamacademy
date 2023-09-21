

def find(string, substring):
    for i in range(len(string)):
        if string[i:i+len(substring)] == substring:
            return i
    return -1


string = input("Enter a string: ")
substring = input("Enter a substring: ")

if find(string, substring) == -1:
    print(f"{substring} is not a substring of {string}")
else:
    print(f"{substring} is a substring of {string}")
