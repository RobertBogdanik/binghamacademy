password = input("Enter your password: ")
if len(password) < 9:
    print("Invalid Password")
    exit()

for i in password:
    if not i.isalnum():
        print("Invalid Password")
        exit()

count = 0
for i in password:
    if i.isdigit():
        count += 1
if count < 2:
    print("Invalid Password")
    exit()

print("Valid Password")