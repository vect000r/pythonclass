length = input("Zapodaj dlugosc:\n")

top = "|"
for i in range(int(length)):
    top += "....|"

bottom = "0"
for i in range(1, int(length) + 1):
    num = str(i)
    spaces = " " * (5 - len(num))
    bottom += spaces + num

ruler = top + "\n" + bottom
print(ruler)