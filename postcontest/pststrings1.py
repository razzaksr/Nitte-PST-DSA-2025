def int_to_roman(num):
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    numerals = ["M", "CM", "D", "CD", "C", "XC",
                "L", "XL", "X", "IX", "V", "IV", "I"]
    result = ""
    for i in range(len(values)):
        count = num // values[i]
        if count:
            result += numerals[i] * count
            num -= values[i] * count    
    return result

test_cases = [1994, 58, 4, 9, 3999, 2024, 1, 1000, 944, 1666]
for i, test in enumerate(test_cases): print(int_to_roman(test))