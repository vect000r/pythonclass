roman_numerals = ['I', 'V', 'X', 'L', 'C', 'D', 'M',
                  'IV', 'IX', 'XL', 'XC', 'CD', 'CM']
arabic_numbers = [1, 5, 10, 50, 100, 500, 1000,
                 4, 9, 40, 90, 400, 900]

# Sposób 1: Użycie zip() i dict()
roman_dict_1 = dict(zip(roman_numerals, arabic_numbers))

# Sposób 2: Dictionary comprehension
roman_dict_2 = {roman: arabic for roman, arabic in zip(roman_numerals, arabic_numbers)}

# Sposób 3: Tradycyjna pętla
roman_dict_3 = {}
for i in range(len(roman_numerals)):
    roman_dict_3[roman_numerals[i]] = arabic_numbers[i]

def roman2int(roman_str):
    result = 0
    prev_value = 0
    
    # Iterujemy od prawej do lewej
    for char in reversed(roman_str.upper()):
        curr_value = roman_dict_1[char]
        
        # Jeśli poprzednia wartość jest większa, dodajemy
        # Jeśli mniejsza, odejmujemy (jak w przypadku IV czy IX)
        if curr_value >= prev_value:
            result += curr_value
        else:
            result -= curr_value
            
        prev_value = curr_value
    
    return result

test =  'MCMXCIV'
print(f"{test} - > {roman2int(test)}")