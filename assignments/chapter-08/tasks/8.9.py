

def binaryToHex(binaryValue):
    decimal = int(binaryValue, 2)

    return hex(decimal)[2:].upper()

userBinary = input("Enter a binary number: ")
print(f"The hex value of {userBinary} is {binaryToHex(userBinary)}")

