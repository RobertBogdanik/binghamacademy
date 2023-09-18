
combination = []

for x in range(1, 8):
    for m in range(1, 8):
        if m == x:
            continue

        if [m, x] in combination:
            continue

        combination.append([x, m])
        print(f"{x} {m}")

print(f"Total combinations: {len(combination)}")