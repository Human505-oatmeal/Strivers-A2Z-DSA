def pattern(n):
    for i in range(1, 2*n):
        stars = i
        if i > n:
            stars = 2*n-i
        print(n * " " + "*" * stars)


pattern(6)
