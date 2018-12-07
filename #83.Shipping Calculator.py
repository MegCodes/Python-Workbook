def shipping_calculator():
    purchased_items = float(input("Please enter amount of items purchased: "))
    price = 0
    if purchased_items == 1:
        price += 10.95
    elif purchased_items > 1:
        price = 2.95 * (purchased_items - 1) + 10.95
    print("The shipping price will amount to ${:.2f}.".format(price))

shipping_calculator()