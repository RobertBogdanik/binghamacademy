decimal = int(input("Enter a decimal number: "))
hexa = ''

while decimal > 0:
    el = str(decimal % 16)
    if el == '10':
        el = 'A'
    elif el == '11':
        el = 'B'
    elif el == '12':
        el = 'C'
    elif el == '13':
        el = 'D'
    elif el == '14':
        el = 'E'
    elif el == '15':
        el = 'F'
    hexa = el + hexa
    decimal //= 16

print(hexa)
