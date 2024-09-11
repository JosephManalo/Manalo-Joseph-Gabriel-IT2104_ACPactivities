def string(s):
    vowels = 'aeiouAEIOU'
    return [char for char in s if char in vowels]
input_string = input("Enter a string: ")
vowel_list = string(input_string)
print(vowel_list)