def is_palindrome(num):
    num_str = str(num)
    return num_str == num_str[::-1]

number = int(input("Enter an integer: "))
if is_palindrome(number):
    print("Palindrome")
else:
    print("Not a Palindrome")
