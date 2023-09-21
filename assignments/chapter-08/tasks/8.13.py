
def prefix(s1, s2):
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return s1[:i]
    return s1

def main():
    s1 = input("Enter a string: ")
    s2 = input("Enter a string: ")
    print(f"The common prefix of {s1} and {s2} is {prefix(s1, s2)}")

