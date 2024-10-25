seq1 = 'aaabdcdbddbjgaashj'
seq2 = 'aabbhdjkkaklgggpp'

a = set()
b = set()

for i in seq1:
    for j in seq2:
        if (i == j):
            a.add(j)

ali = [x for x in a]
print(ali)

for i in seq1:
    for j in seq2:
        b.add(i)
        b.add(j)
bli = [x for x in b]
print(bli)