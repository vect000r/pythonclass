width = input("Podaj szerokosc:\n")
heigth = input("Podaj wysokosc:\n")

top = "+"
for i in range(int(width)):
    top += "---+"

bottom = "|"
for i in range(1, int(width) + 1):
    bottom += "   |"


result = ""
for i in range(int(heigth)):
    result += top + "\n"
    if(i < int(heigth) - 1):
        result += bottom + "\n"
print(result)