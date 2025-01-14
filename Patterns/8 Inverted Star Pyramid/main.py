def pattern(n):
    for i in range(n):
        for j in range(0, i):
            print(" ", end="")

        for j in range(i+1, n*2-i):
            print("*", end="")
        print("")


pattern(6)
