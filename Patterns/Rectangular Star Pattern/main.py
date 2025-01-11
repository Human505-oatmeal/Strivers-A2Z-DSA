def rectangle(n):
    for i in range(n):
        for j in range(n):
            print("*", end="")  # end="" prevents newline after printing "*"
        print()  # Jumps to newline

rectangle(6)
