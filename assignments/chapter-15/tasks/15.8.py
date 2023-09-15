
def reverseDisplay(value):
    if len(value) == 1:
        return value
    else:
        return reverseDisplay(value[1:]) + value[0]
    
userInteger = eval(input("Enter an integer: "))
print(f"Reversed integer: {reverseDisplay(str(userInteger))}")
