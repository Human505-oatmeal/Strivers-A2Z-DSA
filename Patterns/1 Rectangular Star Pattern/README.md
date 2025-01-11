# Rectangular Star Pattern

Python function that generates a **rectangular star pattern** of `n` columns by `n` rows, the pattern will display (`*`)
printed in a grid format.

## Code

```python
def rectangle(n):
    for i in range(n):
        for j in range(n):
            print("*", end="")  # end="" prevents newline after printing "*"
        print()  # Jumps to newline

rectangle(6)  # Call that bad boy
```


## Example Output

if `n = 6`:

```
******
******
******
******
******
******
```