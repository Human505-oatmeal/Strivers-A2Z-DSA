import string  # built-in library you can just do the alphabets in a string though


def pattern(n):
    chars = string.ascii_uppercase
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(chars[j-1], end=" ")
        print()


pattern(6)
