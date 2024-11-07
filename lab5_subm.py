"""
***************************************************************************
Filename:      lab4_subm.py

Author:        Dylan Lam

Date:          10/22/2024

Modifications: Dylan – 10/24/2024

Description:   This module demonstrates the use of functions to:
               1) Take an order for the type and size of the cake from the keyboard(console) interface.
               2) From the inputs gotten from above, using the recipes given here, calculate the amount of each
               ingredient required.
               3) For the cake just selected, print the list of ingredients and each accompanied with the amount in Oz.

***************************************************************************
"""




def print_chocolate_cake(size):
    # chocolate cake ingredients %
    chocolate_flour = 15.8
    chocolate_sugar = 24.5
    chocolate_cp = 5.6
    chocolate_bp = 0.4
    chocolate_bs = 0.6
    chocolate_salt = 0.4
    chocolate_egg = 9
    chocolate_buttermilk = 18
    chocolate_co = 8.1
    chocolate_ve = 0.6
    chocolate_bw = 17

    flour = (chocolate_flour/100) * size
    sugar = (chocolate_sugar/100) * size
    cocoa_powder = (chocolate_cp/100) * size
    baking_powder = (chocolate_bp/100) * size
    baking_soda = (chocolate_bs / 100) * size
    salt = (chocolate_salt / 100) * size
    #baking_powder = (chocolate_bp / 100) * size
    #baking_powder = (chocolate_bp / 100) * size
    #baking_powder = (chocolate_bp / 100) * size
    #baking_powder = (chocolate_bp / 100) * size
    #baking_powder = (chocolate_bp / 100) * size

    print("Flour: {:25.1f} Oz\nSugar: {:25.1f} Oz\nUnsweetened Cocoa Powder: {:6.1f} Oz\nBaking Powder: {:17.1f} Oz"
          "\nBaking Soda: {:19.1f} Oz\nSalt: {:26.1f} Oz\n"
          .format(flour, sugar, cocoa_powder, baking_powder, baking_soda, salt))




def print_red_velvet():
    print("Ingredient A: {:5.1f} Oz\nIngredient B: {:5.1f} Oz\nIngredient C: {:5.1f} Oz"
          "\nIngredient D: {:5.1f} Oz\nIngredient E: {:5.1f} Oz"
          .format(ingredient_a, ingredient_b, ingredient_c, ingredient_d, ingredient_e))




def print_lemon():
    print("Ingredient A: {:5.1f} Oz\nIngredient B: {:5.1f} Oz\nIngredient C: {:5.1f} Oz"
          .format(ingredient_a, ingredient_b, ingredient_c))




# red velvet cake %
red_velvet_a = 22.4
red_velvet_b = 22.4
red_velvet_c = 24.0
red_velvet_d = 17.9
red_velvet_e = 13.3

# lemon cake %
lemon_a = 38.5
lemon_b = 35.8
lemon_c = 25.7

# cake sizes in oz
regular = 64
large = 112

while True:
    customer_cake = input("Please Select Cake Type; Enter 1 for Chocolate, 2 for Red Velvet, 3 for Lemon, q to quit: ")

    if customer_cake == 'q' or customer_cake == 'Q':
        print("Bye!")
        break

    cake_size = input("Please select cake size; Enter L for large, R for regular: ")
    uppercase_letter = cake_size.upper()
    print("")

    customer_cake = int(customer_cake)  #Converting customer cake into an int
    if customer_cake == 1:
        if uppercase_letter == "R":
            print("Regular Chocolate Cake Ingredient list:\n")
            print_chocolate_cake(regular)
        else:
            print("Large Chocolate Cake Ingredient list:\n")
            print_chocolate_cake(large)

    # red velvet cake
    elif customer_cake == 2:
        if uppercase_letter == "R":
            print("Regular Red Velvet Cake Ingredient list:\n")
            ingredient_a = (red_velvet_a / 100) * regular
            ingredient_b = (red_velvet_b / 100) * regular
            ingredient_c = (red_velvet_c / 100) * regular
            ingredient_d = (red_velvet_d / 100) * regular
            ingredient_e = (red_velvet_e / 100) * regular
            print_red_velvet()
        else:
            print("Large Red Velvet Cake Ingredient list:\n")
            ingredient_a = (red_velvet_a / 100) * large
            ingredient_b = (red_velvet_b / 100) * large
            ingredient_c = (red_velvet_c / 100) * large
            ingredient_d = (red_velvet_d / 100) * large
            ingredient_e = (red_velvet_e / 100) * large
            print_red_velvet()

    # lemon cake
    else:
        if uppercase_letter == "R":
            print("Regular Lemon Cake Ingredient list:\n")
            ingredient_a = (lemon_a / 100) * regular
            ingredient_b = (lemon_b / 100) * regular
            ingredient_c = (lemon_c / 100) * regular
            print_lemon()
        else:
            print("Large Lemon Cake Ingredient list:\n")
            ingredient_a = (lemon_a / 100) * large
            ingredient_b = (lemon_b / 100) * large
            ingredient_c = (lemon_c / 100) * large
            print_lemon()