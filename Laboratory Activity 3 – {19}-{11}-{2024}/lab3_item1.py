def roman_to_integer(roman):
    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    integer_value = 0
    prev_value = 0

    for char in roman[::-1]:
        value = roman_values[char.upper()]
        if value < prev_value:
            integer_value -= value
        else:
            integer_value += value
        prev_value = value

    return integer_value

roman = input("Enter a Roman numeral: ")
result = roman_to_integer(roman)
print(f"The integer value of '{roman.upper()}' is: {result}")