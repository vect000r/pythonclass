# Zadanie 2.10#############
print("Zadanie 2.10")
line = "a b\nc\td\nxy"
print(line)
black_line = line.split()
print(len(black_line))
###########################

# Zadanie 2.11 ############
print("Zadanie 2.11")
word = "abcdef"
new_word = "_".join(x for x in word)
print(new_word)
###########################

# Zadanie 2.12 ############
print("Zadanie 2.12")
line_12 = "abc abc abc"
char_list = [x for x in line_12.split()]
first_characters = "".join([x[0] for x in char_list])
last_characters = "".join([x[-1] for x in char_list])
print(first_characters)
print(last_characters)
###########################

# Zadanie 2.13 ############
print("Zadanie 2.13")
line_13 = "abc defg hijkl"
print(sum([len(x) for x in line_13.split()]))
###########################

# Zadanie 2.14 ############
print("Zadanie 2.14")
line_14 = 'abcdef ghi jk l'
a = max([len(x) for x in line_14.split()])
longest = [x for x in line_14.split() if len(x) == a] 
print(f"Najdluzszy wyraz: {''.join(longest[0])}")
print(f"Dlugosc najwyzszego wyrazu: {a}")
###########################

# Zadanie 2.15 ############
print("Zadanie 2.15")
L = [ 1, 2, 3, 4, 5, 6, 7, 8, 9]
Lstr = "".join([str(x) for x in L])
print(Lstr)
###########################

# Zadanie 2.16 ############
print("Zadanie 2.16")
line_16 = "asukjdhajsdhGvRjhasjd"
if "GvR" in line_16:
    new_line_16 = line_16.replace("GvR", "Guido van Rossum")
print(new_line_16)
###########################

# Zadanie 2.17 ############
print("Zadanie 2.17")
line_17 = "jhfda gi ad bhdo"
alph_line_17 = sorted(line_17.split(), key=lambda x: x)
print(f"Posortowane alfabetycznie: {alph_line_17}")
len_line_17 = sorted([s for s in line_17.split()], key= lambda s: len(s))
print(f"Posortowane pod względem długości: {len_line_17}")
###########################

# Zadanie 2.18 ############
print("Zadanie 2.18")
big_num = 89078780007870
str_num = str(big_num)
print(str_num.count("0"))
###########################

# Zadanie 2.19 ############
print("Zadanie 2.19")
L_19 = [1, 10, 100, 2, 20, 200]
result_19 = "".join([str(x).zfill(3) for x in L_19])
print(result_19)
###########################