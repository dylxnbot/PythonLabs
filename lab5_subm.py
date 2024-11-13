"""
***************************************************************************
Filename:      lab5_subm.py

Author:        Dylan Lam

Date:          11/6/2024

Modifications: Dylan – 11/6/2024

Description:   This module demonstrates the use of functions to:
               1) Take an order for the type and size of the cake from the keyboard(console) interface.
               2) From the inputs gotten from above, using the recipes given, calculate the amount of each
               ingredient required in ounces.
               3) For the cake just selected, print the list of ingredients and each accompanied by the amount in Oz.
               4) Uses a sentinel to accept as many cake orders as the user wants.

***************************************************************************
"""




def print_chocolate_cake(size):
    """
    ***************************************************************************

    Function: print_chocolate_cake(size)

    Parameters: size - the size of the cake, regular is 64 and large is 112 oz

    Outputs: A list of 11 strings formatted to "Ingredient   xx.x Oz"

    Returns: None

    Author: Dylan Lam

    Date: 11/6/2024

    Modifications: 11/6/2024

    Description:
    This function takes in one parameter for the size of the cake.
    Then it outputs a list of 11 ingredients and the amount needed in oz to make the cake in either size.

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

    if size == 64:
        print("Regular Chocolate Cake Ingredient list:\n")
    else:
        print("Large Chocolate Cake Ingredient list:\n")


    print("Flour: {:25.1f} Oz\nSugar: {:25.1f} Oz\nUnsweetened Cocoa Powder: {:6.1f} Oz\nBaking Powder: {:17.1f} Oz"
          "\nBaking Soda: {:19.1f} Oz\nSalt: {:26.1f} Oz\nEgg: {:27.1f} Oz\nButtermilk: {:20.1f} Oz"
          "\nOil: {:27.1f} Oz\nVanilla Extract: {:15.1f} Oz\nBoiling Water: {:17.1f} Oz\n"
          .format(flour, sugar, cocoa_powder, baking_powder, baking_soda, salt, egg, buttermilk, canola_oil,
                  vanilla_extract, boiling_water))




def print_red_velvet_cake(size):
    """
    ***************************************************************************

    Function: print_red_velvet_cake(size)

    Parameters: size - the size of the cake, regular is 64 and large is 112 oz

    Outputs: A list of 11 strings formatted to "Ingredient   xx.x Oz"

    Returns: None

    Author: Dylan Lam

    Date: 11/6/2024

    Modifications: 11/6/2024

    Description:
    This function takes in one parameter for the size of the cake.
    Then it outputs a list of 11 ingredients and the amount needed in oz to make the cake in either size.

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

    print("Flour: {:25.1f} Oz\nSugar: {:25.1f} Oz\nUnsweetened Cocoa Powder: {:6.1f} Oz\nBaking Soda: {:19.1f} Oz"
          "\nSalt: {:26.1f} Oz\nEgg: {:27.1f} Oz\nButtermilk: {:20.1f} Oz\nOil: {:27.1f} Oz"
          "\nVanilla Extract: {:15.1f} Oz\nRed Food Coloring: {:13.1f} Oz\nDistilled Vinegar: {:13.1f} Oz\n"
          .format(flour, sugar, cocoa_powder, baking_soda, salt, egg, buttermilk, canola_oil,
                  vanilla_extract, food_coloring, distilled_vinegar))




def print_lemon_cake(size):
    """
    ***************************************************************************

    Function: print_lemon_cake(size)

    Parameters: size - the size of the cake, regular is 64 and large is 112 oz

    Outputs: A list of 10 strings formatted to "Ingredient   xx.x Oz". The Last 4 strings are on a newline and indented

    Returns: None

    Author: Dylan Lam

    Date: 11/6/2024

    Modifications: 11/6/2024

    Description:
    This function takes in one parameter for the size of the cake.
    Then it outputs a list of 10 ingredients and the amount needed in oz to make the cake in either size. The last 4
    strings are on a newline and indented.

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

    print("Butter: {:24.1f} Oz\nSugar: {:25.1f} Oz\nEgg: {:27.1f} Oz\nSifted Self-Rising Flour: {:6.1f} Oz"
          "\nButtermilk: {:20.1f} Oz\nVanilla Extract: {:15.1f} Oz\n"
          "Filling:\n\tEgg Yolk: {:18.1f} Oz\n\tSugar: {:21.1f} Oz\n\tButter: {:20.1f} Oz"
          "\n\tLemon Juice and Zest: {:6.1f} Oz\n"
          .format(butter, sugar, egg, sifted_flour, buttermilk, vanilla_extract, filling_egg_yolk,
                  filling_sugar, filling_butter, filling_lemon_juice_zest))




# cake sizes in oz
regular = 64
large = 112

while True:
    customer_cake = input("Please Select Cake Type; Enter 1 for Chocolate, 2 for Red Velvet, 3 for Lemon, q to quit: ")

    if customer_cake == 'q' or customer_cake == 'Q':
        print("Bye!")
        break

    cake_size = input("Please select cake size; Enter L for large, R for regular: ")
    # Making it so that letters are made into uppercase making it easier when reading if uppercase_letter is "r" or "l"
    # instead of "r or R" or "l or L"
    uppercase_letter = cake_size.upper()
    print("")

    # Converting customer_cake into an int
    customer_cake = int(customer_cake)

    # Chocolate cake
    if customer_cake == 1:
        # Regular sized cake
        if uppercase_letter == "R":
            print_chocolate_cake(regular)
        # Large sized cake
        else:
            print_chocolate_cake(large)

    # Red velvet cake
    elif customer_cake == 2:
        if uppercase_letter == "R":
            print("Regular Red Velvet Cake Ingredient list:\n")
            print_red_velvet_cake(regular)
        else:
            print("Large Red Velvet Cake Ingredient list:\n")
            print_red_velvet_cake(large)

    # Lemon cake
    else:
        if uppercase_letter == "R":
            print("Regular Lemon Cake Ingredient list:\n")
            print_lemon_cake(regular)
        else:
            print("Large Lemon Cake Ingredient list:\n")
            print_lemon_cake(large)




"""
This is the record of execution

C:\\PycharmProjects\\.venv\\Scripts\\python.exe C:\\PycharmProjects\\pythonProject\\lab5_subm.py 
Please Select Cake Type; Enter 1 for Chocolate, 2 for Red Velvet, 3 for Lemon, q to quit: 2
Please select cake size; Enter L for large, R for regular: l

Large Red Velvet Cake Ingredient list:

Flour:                      25.1 Oz
Sugar:                      25.1 Oz
Unsweetened Cocoa Powder:    0.4 Oz
Baking Soda:                 0.8 Oz
Salt:                        0.4 Oz
Egg:                        10.1 Oz
Buttermilk:                 20.0 Oz
Oil:                        26.9 Oz
Vanilla Extract:             0.3 Oz
Red Food Coloring:           2.4 Oz
Distilled Vinegar:           0.4 Oz

Please Select Cake Type; Enter 1 for Chocolate, 2 for Red Velvet, 3 for Lemon, q to quit: 3
Please select cake size; Enter L for large, R for regular: r

Regular Lemon Cake Ingredient list:

Butter:                      5.4 Oz
Sugar:                       9.6 Oz
Egg:                         5.8 Oz
Sifted Self-Rising Flour:   10.0 Oz
Buttermilk:                  5.8 Oz
Vanilla Extract:             0.1 Oz
Filling:
	Egg Yolk:               11.5 Oz
	Sugar:                   7.2 Oz
	Butter:                  1.3 Oz
	Lemon Juice and Zest:    7.3 Oz

Please Select Cake Type; Enter 1 for Chocolate, 2 for Red Velvet, 3 for Lemon, q to quit: 3
Please select cake size; Enter L for large, R for regular: l

Large Lemon Cake Ingredient list:

Butter:                      9.5 Oz
Sugar:                      16.8 Oz
Egg:                        10.1 Oz
Sifted Self-Rising Flour:   17.5 Oz
Buttermilk:                 10.1 Oz
Vanilla Extract:             0.2 Oz
Filling:
	Egg Yolk:               20.0 Oz
	Sugar:                  12.7 Oz
	Butter:                  2.4 Oz
	Lemon Juice and Zest:   12.8 Oz

Please Select Cake Type; Enter 1 for Chocolate, 2 for Red Velvet, 3 for Lemon, q to quit: 1
Please select cake size; Enter L for large, R for regular: r

Regular Chocolate Cake Ingredient list:

Flour:                      10.1 Oz
Sugar:                      15.7 Oz
Unsweetened Cocoa Powder:    3.6 Oz
Baking Powder:               0.3 Oz
Baking Soda:                 0.4 Oz
Salt:                        0.3 Oz
Egg:                         5.8 Oz
Buttermilk:                 11.5 Oz
Oil:                         5.2 Oz
Vanilla Extract:             0.4 Oz
Boiling Water:              10.9 Oz

Please Select Cake Type; Enter 1 for Chocolate, 2 for Red Velvet, 3 for Lemon, q to quit: 1
Please select cake size; Enter L for large, R for regular: r

Regular Chocolate Cake Ingredient list:

Flour:                      10.1 Oz
Sugar:                      15.7 Oz
Unsweetened Cocoa Powder:    3.6 Oz
Baking Powder:               0.3 Oz
Baking Soda:                 0.4 Oz
Salt:                        0.3 Oz
Egg:                         5.8 Oz
Buttermilk:                 11.5 Oz
Oil:                         5.2 Oz
Vanilla Extract:             0.4 Oz
Boiling Water:              10.9 Oz

Please Select Cake Type; Enter 1 for Chocolate, 2 for Red Velvet, 3 for Lemon, q to quit: q
Bye!

Process finished with exit code 0

"""