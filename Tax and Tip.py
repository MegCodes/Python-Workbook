#Vers.1
def restauraunt_bill():
    meal_cost = float(input("Enter a meal cost: "))
    tax = meal_cost * 0.5
    tip = meal_cost * 0.18
    total = meal_cost + tax + tip
    print("\nTax is: %.2f \nTip is: %.2f \nTotal: %.2f" % (tax, tip, total))
    
restauraunt_bill()   

#Vers.2
def restauraunt_bill(meal_cost):
    tax = meal_cost * 0.5
    tip = meal_cost * 0.18
    total = meal_cost + tax + tip
    print("\nTax is: %.2f \nTip is: %.2f \nTotal: %.2f" % (tax, tip, total))
    
restauraunt_bill(23.8)    
restauraunt_bill(60.00)
restauraunt_bill(268.70)