def is_perfect_number(num):
    if num < 1:
        return False
    divisors_sum = 0
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            divisors_sum += i
    return divisors_sum == num

if __name__ == "__main__":
    try:
        number = input("Enter a number: ")
        num = int(number)
        if is_perfect_number(num):
            print(f"{num} is a perfect number.")
        else:
            print(f"{num} is not a perfect number.")
    except ValueError:
        print("Please enter a valid integer")
