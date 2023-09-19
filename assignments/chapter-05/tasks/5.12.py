cursor = 100
inline = 0
while cursor < 1000:
    if cursor % 5 == 0 and cursor % 6 == 0:
        print(cursor, end=" ")
        inline += 1
        if inline == 10:
            inline = 0
            print("")
    cursor += 1
