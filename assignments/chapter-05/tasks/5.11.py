f = open("../dziwne/score.txt", "r")
scores = []
for x in f:
    x = x.replace("\n", "")
    scores.append(int(x))

scores.sort()
print(scores[-1])

