userNumbers = input("Enter a list of numbers: ")
userNumbers = [int(x) for x in userNumbers.split()]
distinctNumbers = list(set(userNumbers))

most = {
    "numbers": [],
    "value": 0
}

for number in distinctNumbers:
    if userNumbers.count(number) > most["value"]:
        most["numbers"] = [number]
        most["value"] = userNumbers.count(number)
    elif userNumbers.count(number) == most["value"]:
        most["numbers"].append(number)

print(f"The most frequent numbers are {most['numbers']} with {most['value']} occurrences")

