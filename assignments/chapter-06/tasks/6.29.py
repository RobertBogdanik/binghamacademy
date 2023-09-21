cardNumber = eval(input("Enter a credit card number as a long integer: "))

def getDigit(number):
    if number < 10:
        return number
    else:
        return number % 10 + number // 10

# Get the result from Step 2
def sumOfDoubleEvenPlace(number):
    digits = []
    for i in range(len(str(number))):
        if i % 2 == 0:
            digits.append(int(str(number)[i]))

    res = []
    for dig in digits:
        res.append(getDigit(dig * 2))


    return sum(res)

# Return sum of odd place digits in number
def sumOfOddPlace(number):
    digits = []
    for i in range(len(str(number))):
        if i % 2 != 0:
            digits.append(int(str(number)[i]))

    return sum(digits)


# Return true if the digit d is a prefix for number
def prefixMatched(number, d):
    if getPrefix(number, getSize(d)) == d:
        return True

    return False

def getSize(d):
    return len(str(d))

def getPrefix(number, k):
    if len(str(number)) < k:
        return number

    return number[:k]



def isValid(number):
    if (sumOfDoubleEvenPlace(number) + sumOfOddPlace(number)) % 10 == 0:
        return True
    else:
        return False

print(isValid(cardNumber))