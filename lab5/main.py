import fracs

if __name__ == "__main__":
    frac2 = [1, 4]
    frac1 = [1, 3]
    print(fracs.add_frac(frac1, frac2))
    print(fracs.sub_frac(frac1, frac2))
    print(fracs.mul_frac(frac1, frac2))
    print(fracs.div_frac(frac1, frac2))
    print(fracs.cmp_frac(frac1, frac2))
    print(fracs.is_positive(frac1))
    print(fracs.is_zero(frac1))