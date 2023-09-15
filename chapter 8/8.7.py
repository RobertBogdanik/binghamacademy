def getNumber(uppercase_letter):
    letter = uppercase_letter.lower()
    match letter:
        case 'a' | 'b' | 'c':
            return 2
        case 'd' | 'e' | 'f':
            return 3
        case 'g' | 'h' | 'i':
            return 4
        case 'j' | 'k' | 'l':
            return 5
        case 'm' | 'n' | 'o':
            return 6
        case 'p' | 'q' | 'r' | 's':
            return 7
        case 'w' | 'x' | 'y' | 'z':
            return 8
        case _:
            return letter


phone_number = str(input("Enter a string: "))

number = ''
for letter in phone_number:
    number += str(getNumber(letter))

print(number)