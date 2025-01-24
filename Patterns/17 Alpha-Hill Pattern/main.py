import string


def pattern(n):
    char = string.ascii_uppercase
    for i in range(1, n+1):
        for j in range(n-i):
            print(" ", end="")

        for j in range(1, i*2):
            if j == i and i != 1:  # gets the midpoint
                midpoint = j
                print(f"{char[midpoint-1]}", end="")

                for k in range(midpoint-2, -1, -1):
                    print(f"{char[k]}", end="")
                break
            else:
                print(f"{char[j-1]}", end="")

        for j in range(n-i):
            print(" ", end="")

        print()


pattern(6)
