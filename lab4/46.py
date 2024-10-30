def sum_seq(sequence):
    result = 0
    for seq in sequence:
        if isinstance(seq, (list, tuple)):
            result += sum_seq(seq)
        else:
            result += seq
    return result

seq = [1,(2,3),[],[4,(5,6,7)],8,[9]]
print(sum_seq(seq))