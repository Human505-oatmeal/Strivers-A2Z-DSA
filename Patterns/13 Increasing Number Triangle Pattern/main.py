def pattern(n):
    num = 0
    for i in range(1, n+1):
        for j in range(1, i+1):
            num += 1
            print(f"{num} ", end="")
        print()


pattern(6)