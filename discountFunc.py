#Part 1
def calculate_discount(original_price, discount_percent):
    final_price = original_price - (original_price * (discount_percent / 100))

    if discount_percent >= 20:
        print("Final price after discount: {:.2f}".format(final_price))
    else:
        print("Original price(without significant discount): {:.2f}".format(original_price))

calculate_discount(original_price=300, discount_percent=50)


#Part 2
def calculate_discount(original_price, discount_percent):
    discount_amount = original_price * (discount_percent / 100)
    final_price = original_price - discount_amount
    if discount_percent >= 20:
        print("Final price after discount: {:.2f}".format(final_price))
    else:
        print("Original price: {:.2f}".format(final_price))
#take input from user
original_price = float(input('Enter the original price: '))
discount_percent = float(input('Enter the discount on item: '))
#call the function
calculate_discount(original_price, discount_percent)