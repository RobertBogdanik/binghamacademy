def decimalToBinary(value):
    return bin(value)[2:]

userDecimal = int(input("Enter a decimal number: "))
print(f"The binary value of {userDecimal} is {decimalToBinary(userDecimal)}")
