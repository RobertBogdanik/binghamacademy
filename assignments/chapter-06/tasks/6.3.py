def isPalindrome(number):
    return number == reverse(number)

def reverse(number):
    return int(str(number)[::-1])

userNumber = eval(input("Enter a number: "))
print(f"Is {userNumber} a palindrome? {isPalindrome(userNumber)}")
