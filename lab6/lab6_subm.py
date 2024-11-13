"""
***************************************************************************
Filename:      lab6_subm.py

Author:        Dylan Lam

Date:          11/12/2024

Modifications: Dylan – 11/12/2024

Description:   This module demonstrates the use of functions to:
               1) Take an order for the type and size of the cake from the keyboard(console) interface.
               2) From the inputs gotten from above, using the recipes given, calculate the amount of each
               ingredient required in ounces.
               3) For the cake just selected, print the list of ingredients and each accompanied by the amount in Oz.
               4) Uses a sentinel to accept as many cake orders as the user wants.
               5) Writes output to file cake_ingredient_list.txt

***************************************************************************
"""




def print_chocolate_cake(size, write_file):
    """
    ***************************************************************************

    Function: print_chocolate_cake(size, write_file)

    Parameters: size - the size of the cake, regular is 64 and large is 112 oz
                write_file - the file object to which the output will be written

    Outputs: Writes a list of 11 ingredients and their respective amounts in ounces
             to the provided file object, formatted as "Ingredient   xx.x Oz"

    Returns: None

    Author: Dylan Lam

    Date: 11/6/2024

    Modifications: 11/12/2024

    Description:
    This function takes in two parameters: the size of the cake and a file  object to write to. It calculates the
    amount of each ingredient needed based on the given size and writes a formatted ingredient list to the file object.

    ***************************************************************************
    """
    # chocolate cake ingredients %
    chocolate_flour = 15.8
    chocolate_sugar = 24.5
    chocolate_ucp = 5.6
    chocolate_bp = 0.4
    chocolate_bs = 0.6
    chocolate_salt = 0.4
    chocolate_egg = 9
    chocolate_buttermilk = 18
    chocolate_co = 8.1
    chocolate_ve = 0.6
    chocolate_bw = 17

    flour = (chocolate_flour / 100) * size
    sugar = (chocolate_sugar / 100) * size
    cocoa_powder = (chocolate_ucp / 100) * size
    baking_powder = (chocolate_bp / 100) * size
    baking_soda = (chocolate_bs / 100) * size
    salt = (chocolate_salt / 100) * size
    egg = (chocolate_egg / 100) * size
    buttermilk = (chocolate_buttermilk / 100) * size
    canola_oil = (chocolate_co / 100) * size
    vanilla_extract = (chocolate_ve / 100) * size
    boiling_water = (chocolate_bw / 100) * size

    # Checking the size of the cake and updating cake_size_text
    if size == 64:
        cake_size_text = "Regular Chocolate Cake Ingredient list:\n"
    else:
        cake_size_text = "Large Chocolate Cake Ingredient list:\n"

    # Assigning ingredient_text to the string
    ingredient_text = (
        f"Flour: {flour:25.1f} Oz\n"
        f"Sugar: {sugar:25.1f} Oz\n"
        f"Unsweetened Cocoa Powder: {cocoa_powder:6.1f} Oz\n"
        f"Baking Powder: {baking_powder:17.1f} Oz\n"
        f"Baking Soda: {baking_soda:19.1f} Oz\n"
        f"Salt: {salt:26.1f} Oz\n"
        f"Egg: {egg:27.1f} Oz\n"
        f"Buttermilk: {buttermilk:20.1f} Oz\n"
        f"Oil: {canola_oil:27.1f} Oz\n"
        f"Vanilla Extract: {vanilla_extract:15.1f} Oz\n"
        f"Boiling Water: {boiling_water:17.1f} Oz\n"
        )

    # Printing the strings into the open file cake_ingredient_list.txt
    write_file.write(cake_size_text)
    write_file.write(ingredient_text + "\n")




def print_red_velvet_cake(size, write_file):
    """
    ***************************************************************************

    Function: print_red_velvet_cake(size, write_file)

    Parameters: size - the size of the cake, regular is 64 and large is 112 oz
                write_file - the file object to which the output will be written

    Outputs: Writes a list of 11 ingredients and their respective amounts in ounces
             to the provided file object, formatted as "Ingredient   xx.x Oz"

    Returns: None

    Author: Dylan Lam

    Date: 11/6/2024

    Modifications: 11/12/2024

    Description:
    This function takes in two parameters: the size of the cake and a file  object to write to. It calculates the
    amount of each ingredient needed based on the given size and writes a formatted ingredient list to the file object.

    ***************************************************************************
    """
    # red velvet cake ingredients %
    rv_flour = 22.4
    rv_sugar = 22.4
    rv_bs = 0.7
    rv_salt = 0.4
    rv_ucp = 0.4
    rv_co = 24
    rv_buttermilk = 17.9
    rv_egg = 9
    rv_rfc = 2.1
    rv_ve = 0.3
    rv_dv = 0.4

    flour = (rv_flour / 100) * size
    sugar = (rv_sugar / 100) * size
    baking_soda = (rv_bs / 100) * size
    salt = (rv_salt / 100) * size
    cocoa_powder = (rv_ucp / 100) * size
    canola_oil = (rv_co / 100) * size
    buttermilk = (rv_buttermilk / 100) * size
    egg = (rv_egg / 100) * size
    food_coloring = (rv_rfc / 100) * size
    vanilla_extract = (rv_ve / 100) * size
    distilled_vinegar = (rv_dv / 100) * size

    # Checking the size of the cake and updating cake_size_text
    if size == 64:
        cake_size_text = "Regular Red Velvet Cake Ingredient list:\n"
    else:
        cake_size_text = "Large Red Velvet Cake Ingredient list:\n"

    # Assigning ingredient_text to the string
    ingredient_text = (
        f"Flour: {flour:25.1f} Oz\n"
        f"Sugar: {sugar:25.1f} Oz\n"
        f"Unsweetened Cocoa Powder: {cocoa_powder:6.1f} Oz\n"
        f"Baking Soda: {baking_soda:19.1f} Oz\n"
        f"Salt: {salt:26.1f} Oz\n"
        f"Egg: {egg:27.1f} Oz\n"
        f"Buttermilk: {buttermilk:20.1f} Oz\n"
        f"Oil: {canola_oil:27.1f} Oz\n"
        f"Vanilla Extract: {vanilla_extract:15.1f} Oz\n"
        f"Red Food Coloring: {food_coloring:13.1f} Oz\n"
        f"Distilled Vinegar: {distilled_vinegar:13.1f} Oz\n"
          )

    # Printing the strings into the open file cake_ingredient_list.txt
    write_file.write(cake_size_text)
    write_file.write(ingredient_text + "\n")




def print_lemon_cake(size, write_file):
    """
    ***************************************************************************

    Function: print_lemon_cake(size, write_file)

    Parameters: size - the size of the cake, regular is 64 and large is 112 oz
                write_file - the file object to which the output will be written

    Outputs: Writes a list of 10 ingredients and their respective amounts in ounces
             to the provided file object, formatted as "Ingredient   xx.x Oz".
             The Last 4 strings are on a newline and indented.

    Returns: None

    Author: Dylan Lam

    Date: 11/6/2024

    Modifications: 11/12/2024

    Description:
    This function takes in two parameters: the size of the cake and a file  object to write to. It calculates the
    amount of each ingredient needed based on the given size and writes a formatted ingredient list to the file object.
    The last 4 ingredients are on a new line and indented.

    ***************************************************************************
    """
    # lemon cake ingredients %
    lemon_butter = 8.5
    lemon_sugar = 15
    lemon_egg = 9
    lemon_sifted_flour = 15.6
    lemon_buttermilk = 9
    lemon_ve = 0.2
    lemon_filling_egg_yolk = 17.9
    lemon_filling_sugar = 11.3
    lemon_filling_butter = 2.1
    lemon_filling_lemon = 11.4

    butter = (lemon_butter / 100) * size
    sugar = (lemon_sugar / 100) * size
    egg = (lemon_egg / 100) * size
    sifted_flour = (lemon_sifted_flour / 100) * size
    buttermilk = (lemon_buttermilk / 100) * size
    vanilla_extract = (lemon_ve / 100) * size
    filling_egg_yolk = (lemon_filling_egg_yolk / 100) * size
    filling_sugar = (lemon_filling_sugar / 100) * size
    filling_butter = (lemon_filling_butter / 100) * size
    filling_lemon_juice_zest = (lemon_filling_lemon / 100) * size

    # Checking the size of the cake and updating cake_size_text
    if size == 64:
        cake_size_text = "Regular Lemon Cake Ingredient list:\n"
    else:
        cake_size_text = "Large Lemon Cake Ingredient list:\n"

    # Assigning ingredient_text to the string
    ingredient_text = (
        f"Butter: {butter:24.1f} Oz\n"
        f"Sugar: {sugar:25.1f} Oz\n"
        f"Egg: {egg:27.1f} Oz\n"
        f"Sifted Self-Rising Flour: {sifted_flour:6.1f} Oz\n"
        f"Buttermilk: {buttermilk:20.1f} Oz\n"
        f"Vanilla Extract: {vanilla_extract:15.1f} Oz\n"
        f"Filling:\n\tEgg Yolk: {filling_egg_yolk:18.1f} Oz\n\t"
        f"Sugar: {filling_sugar:21.1f} Oz\n\t"
        f"Butter: {filling_butter:20.1f} Oz\n\t"
        f"Lemon Juice and Zest: {filling_lemon_juice_zest:6.1f} Oz\n"
          )

    # Printing the strings into the open file cake_ingredient_list.txt
    write_file.write(cake_size_text)
    write_file.write(ingredient_text + "\n")




# Cake sizes in oz
regular = 64
large = 112


# Opening a new file then running the sentinel loop
with open("cake_orders.txt", "r") as order_file, open("cake_ingredient_list.txt", "w") as write_file:
    while True:
        cake_type = order_file.read(1)
        if cake_type == '':
            break
        order_file.read(3)  # Skip the 3 spaces
        cake_size = order_file.read(1)
        order_file.read(1)  # Skip the newline character

        size = large if cake_size == 'L' else regular

        if cake_type == '1':
            print_chocolate_cake(size, write_file)
        elif cake_type == '2':
            print_red_velvet_cake(size, write_file)
        elif cake_type == '3':
            print_lemon_cake(size, write_file)