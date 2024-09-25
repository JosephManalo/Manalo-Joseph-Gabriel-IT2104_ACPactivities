def calculate_discount(purchase_amount):
    if purchase_amount > 5000:
        discount_rate = 0.10
    else:
        discount_rate = 0.05

    discount = purchase_amount * discount_rate
    final_amount = purchase_amount - discount
    return final_amount, discount

while True:
        amount = float(input("Enter the total purchase amount: "))
        final_amount, discount = calculate_discount(amount)

        print(f"Initial Purchase Amount: {amount:.2f}")
        print(f"Discount: {discount:.2f}")
        print(f"Final Price: {final_amount:.2f}")

        retry = input("Do you want to try again? (yes/no): ").strip().lower()
        if retry != 'yes':
            print("Thank you!")
            break

