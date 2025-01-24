import string


def pattern(n):
    char = string.ascii_uppercase
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(char[i-1], end=" ")
        print()


pattern(6)
