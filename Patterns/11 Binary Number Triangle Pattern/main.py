def pattern(n):
    for i in range(n+1):
        if i % 2 == 0:
            start = 1
        else:
            start = 0
        for j in range(i+1):
            print(f"{start} ", end="")
            start = 1 - start
        print()


pattern(5)
