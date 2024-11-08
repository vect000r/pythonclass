import math

def gcd(a, b):
    return math.gcd(a, b)

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def adjust_fractions(frac1, frac2):
    factor1 = lcm(frac1[1], frac2[1]) // frac1[1]
    factor2 = lcm(frac1[1], frac2[1]) // frac2[1]
    return factor1, factor2, lcm(frac1[1], frac2[1])

def add_frac(frac1, frac2):
    if frac1[1] == frac2[1]:
        return [frac1[0] + frac2[0], frac1[1]]
    else:
        factor1, factor2, lcm_val = adjust_fractions(frac1, frac2)
        new_frac = (frac1[0] * factor1) + (frac2[0] * factor2)
        return reduce_fraction([new_frac, lcm_val])

def sub_frac(frac1, frac2):
    if frac1[1] == frac2[1]:
        if frac1[0] >= frac2[0]:
            return [frac1[0] - frac2[0], frac1[1]]
        else:
            return [frac2[0] - frac1[0], frac1[1]]
    else:
        factor1, factor2, lcm_val = adjust_fractions(frac1, frac2)
        new_frac = (frac1[0] * factor1) - (frac2[0] * factor2)
        return reduce_fraction([new_frac, lcm_val])

def mul_frac(frac1, frac2):
    return reduce_fraction([frac1[0] * frac2[0], frac1[1] * frac2[1]])

def div_frac(frac1, frac2):
    return reduce_fraction([frac1[0] * frac2[1], frac1[1] * frac2[0]])

def is_positive(frac):
    return True if frac[0] >= 0 else False

def is_zero(frac):
    return True if frac[0] == 0 else False

def cmp_frac(frac1, frac2):
    factor1, factor2, lcm_val = adjust_fractions(frac1, frac2)
    adjusted_num1 = frac1[0] * factor1
    adjusted_num2 = frac2[0] * factor2
    if adjusted_num1 < adjusted_num2:
        return -1
    elif adjusted_num1 == adjusted_num2:
        return 0
    else:
        return 1

def frac2float(frac):
    return float(frac[0] / frac[1])

def reduce_fraction(frac):
    gcd_val = gcd(frac[0], frac[1])
    return [frac[0] // gcd_val, frac[1] // gcd_val]