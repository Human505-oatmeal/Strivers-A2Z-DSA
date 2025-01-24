import string


def pattern(n):
    char = string.ascii_uppercase
    for i in range(1, n+1):
        for j in range(n - i):
            print(char[j], end=" ")
        print()


pattern(6)
