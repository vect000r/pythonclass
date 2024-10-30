def make_ruler(n: int) -> str:
    top = "|"
    for i in range(n):
        top += "....|"

    bottom = "0"
    for i in range(1, n + 1):
        num = str(i)
        spaces = " " * (5 - len(num))
        bottom += spaces + num

    ruler = top + "\n" + bottom
    return ruler

def make_grid(rows: int, cols: int) -> str:
    top = "+"
    for i in range(rows):
        top += "---+"

    bottom = "|"
    for i in range(1, rows + 1):
        bottom += "   |"


    grid = ""
    for i in range(cols):
        grid += top + "\n"
        if(i < cols - 1):
            grid += bottom + "\n"
    return grid


print(make_ruler(20))
print(make_grid(5,5))