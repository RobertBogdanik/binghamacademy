
def count(s, a):
    if len(s) == 1:
        if s == a:
            return 1
        else:
            return 0
    else:
        if s[0] == a:
            return 1 + count(s[1:], a)
        else:
            return count(s[1:], a)
        
userString = input("Enter string: ")
userChar = input("Enter character: ")
print(f"Number of occurrences of {userChar} in {userString} is {count(userString, userChar)}")
