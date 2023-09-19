numbers = eval(input("Enter the number of students: "))
i = 0
scores = []

while i<numbers:
    score = eval(input(f"Enter score for student {i}: "))
    scores.append(score)
    i += 1

scores.sort()
scores = scores[::-1]

print(scores[0], scores[1])
