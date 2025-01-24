def pattern(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(j, end="")
        for j in range(n*2-(i*2)):
            print(" ", end="")
        for j in range(i, 0, -1):
            print(j, end="")
        print()


pattern(6)

'''
Probably not the best way to go about it but I feel like this approach is pretty simple and straight-forward, 
essentially just focusing on the first inner loop and then connecting the space logic and then the third inner loop
which just starts from i and decrements -1...
'''