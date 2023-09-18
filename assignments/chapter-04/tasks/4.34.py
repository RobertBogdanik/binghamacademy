hex = input("Enter a hex digit: ")

if hex.upper() in ("A", "B", "C", "D", "E", "F") or int(hex) < 10:
    print(f"The hex value is {int(hex, 16)}")
else:
    print("Invalid input")
