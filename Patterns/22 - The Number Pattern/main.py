def pattern(n):
    for i in range(1, (n*2)):
        for j in range(1, (n*2)):
            top = i - 1
            left = j - 1
            right = (2*n - 1) - j
            down = (2*n - 1) - i
            print(n - min(top, left, right, down), end=" ")
        print()

pattern(5)
