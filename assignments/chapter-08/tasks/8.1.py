import re

ssn = input("Enter a SSN: \n")
pattern = re.compile(r"\d{3}-\d{2}-\d{4}")

if pattern.match(ssn):
    print("Valid SSN")
else:
    print("Invalid SSN")
