def flatten(sequence):
    result = []
    for seq in sequence:
        if isinstance(seq, (list, tuple)):
            result.extend(flatten(seq))
        else:
            result.append(seq)
    return result

seq = [1,(2,3),[],[4,(5,6,7)],8,[9]]
print(flatten(seq))   # [1,2,3,4,5,6,7,8,9]
