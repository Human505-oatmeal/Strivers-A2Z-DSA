def pattern(n):
    for i in range(0, n):
        for j in range(0, n-i):
            print("*", end="")
        for j in range(0, i*2):
            print(" ", end="")
        for j in range(0, n-i):
            print("*", end="")
        print()

    for i in range(n-2, -1, -1):
        for j in range(0, n-i):
            print("*", end="")
        for j in range(0, i*2):
            print(" ", end="")
        for j in range(0, n-i):
            print("*", end="")
        print()


pattern(8)
