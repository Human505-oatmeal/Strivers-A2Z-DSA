import string


def pattern(n):
    char = string.ascii_uppercase[0:n]
    for i in range(1, n+1):
        print(" ".join(char[-i:]))


pattern(6)
