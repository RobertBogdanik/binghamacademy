import re

def count(s1, s2):
    return len(re.findall(s2, s1))

str1 = input("Enter a string: ")
str2 = input("Enter a substring: ")
print(count(str1, str2))
