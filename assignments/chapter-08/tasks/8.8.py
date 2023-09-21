def binaryToDecimal(binaryString):
    decimal = 0
    for i in range(len(binaryString)):
        decimal = decimal * 2 + int(binaryString[i])
    return decimal


print(binaryToDecimal("10001"))
