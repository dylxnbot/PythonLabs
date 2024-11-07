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




def print_chocolate():
    """
    ***************************************************************************

    Function: print_chocolate()

    Parameters: none

    Outputs: A string containing 4 ingredients formatted to "Ingredient X  xx.x Oz"

    Returns: None

    Author: Dylan Lam

    Date: 10/22/2024

    Modifications: 10/24/2024

    Description:
    This function outputs a string containing the ingredients that were calculated before the function was called.

    ***************************************************************************
    """
    print("Ingredient A: {:5.1f} Oz\nIngredient B: {:5.1f} Oz\nIngredient C: {:5.1f} Oz\nIngredient D: {:5.1f} Oz"
          .format(ingredient_a, ingredient_b, ingredient_c, ingredient_d))




def print_red_velvet():
    """
    ***************************************************************************

    Function: print_red_velvet()

    Parameters: none

    Outputs: A string containing 5 ingredients formatted to "Ingredient X  xx.x Oz"

    Returns: None

    Author: Dylan Lam

    Date: 10/22/2024

    Modifications: 10/24/2024

    Description:
    This function outputs a string containing the ingredients that were calculated before the function was called.

    ***************************************************************************
    """
    print("Ingredient A: {:5.1f} Oz\nIngredient B: {:5.1f} Oz\nIngredient C: {:5.1f} Oz"
          "\nIngredient D: {:5.1f} Oz\nIngredient E: {:5.1f} Oz"
          .format(ingredient_a, ingredient_b, ingredient_c, ingredient_d, ingredient_e))




def print_lemon():
    """
    ***************************************************************************

    Function: print_lemon()

    Parameters: none

    Outputs: A string containing 3 ingredients formatted to "Ingredient X  xx.x Oz"

    Returns: None

    Author: Dylan Lam

    Date: 10/22/2024

    Modifications: 10/24/2024

    Description:
    This function outputs a string containing the ingredients that were calculated before the function was called.

    ***************************************************************************
    """
    print("Ingredient A: {:5.1f} Oz\nIngredient B: {:5.1f} Oz\nIngredient C: {:5.1f} Oz"
          .format(ingredient_a, ingredient_b, ingredient_c))




# chocolate cake %
chocolate_a = 15.8
chocolate_b = 24.5
chocolate_c = 5.6
chocolate_d = 54.1

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

# user input
customer_cake = int(input("Please select cake type; Enter 1 for Chocolate, 2 for Red Velvet and 3 for Lemon: "))
print("")
cake_size = input("Please select cake size; Enter L for large, R for regular: ")
uppercase_letter = cake_size.upper()
print("")

# chocolate cake
if customer_cake == 1:
    if uppercase_letter == "R":
        print("Regular Chocolate Ingredient list:")
        ingredient_a = (chocolate_a / 100) * regular
        ingredient_b = (chocolate_b / 100) * regular
        ingredient_c = (chocolate_c / 100) * regular
        ingredient_d = (chocolate_d / 100) * regular
        print_chocolate()
    else:
        print("Large Chocolate Ingredient list:")
        ingredient_a = (chocolate_a / 100) * large
        ingredient_b = (chocolate_b / 100) * large
        ingredient_c = (chocolate_c / 100) * large
        ingredient_d = (chocolate_d / 100) * large
        print_chocolate()

# red velvet cake
elif customer_cake == 2:
    if uppercase_letter == "R":
        print("Regular Red Velvet Ingredient list:")
        ingredient_a = (red_velvet_a / 100) * regular
        ingredient_b = (red_velvet_b / 100) * regular
        ingredient_c = (red_velvet_c / 100) * regular
        ingredient_d = (red_velvet_d / 100) * regular
        ingredient_e = (red_velvet_e / 100) * regular
        print_red_velvet()
    else:
        print("Large Red Velvet Ingredient list:")
        ingredient_a = (red_velvet_a / 100) * large
        ingredient_b = (red_velvet_b / 100) * large
        ingredient_c = (red_velvet_c / 100) * large
        ingredient_d = (red_velvet_d / 100) * large
        ingredient_e = (red_velvet_e / 100) * large
        print_red_velvet()

# lemon cake
else:
    if uppercase_letter == "R":
        print("Regular Lemon Ingredient list:")
        ingredient_a = (lemon_a / 100) * regular
        ingredient_b = (lemon_b / 100) * regular
        ingredient_c = (lemon_c / 100) * regular
        print_lemon()
    else:
        print("Large Lemon Ingredient list:")
        ingredient_a = (lemon_a / 100) * large
        ingredient_b = (lemon_b / 100) * large
        ingredient_c = (lemon_c / 100) * large
        print_lemon()

"""
This is the record of execution

C:\\PycharmProjects\\.venv\\Scripts\\python.exe C:\\PycharmProjects\\pythonProject\\la4_subm.py
Please select cake type; Enter 1 for Chocolate, 2 for Red Velvet and 3 for Lemon: 1

Please select cake size; Enter L for large, R for regular: L

Large Chocolate Ingredient list:
Ingredient A:  17.7 Oz
Ingredient B:  27.4 Oz
Ingredient C:   6.3 Oz
Ingredient D:  60.6 Oz

Process finished with exit code 0



C:\\PycharmProjects\\.venv\\Scripts\\python.exe C:\\PycharmProjects\\pythonProject\\la4_subm.py 
Please select cake type; Enter 1 for Chocolate, 2 for Red Velvet and 3 for Lemon: 3

Please select cake size; Enter L for large, R for regular: r

Regular Lemon Ingredient list:
Ingredient A:  24.6 Oz
Ingredient B:  22.9 Oz
Ingredient C:  16.4 Oz

Process finished with exit code 0



C:\\PycharmProjects\\.venv\\Scripts\\python.exe C:\\PycharmProjects\\pythonProject\\la4_subm.py 
Please select cake type; Enter 1 for Chocolate, 2 for Red Velvet and 3 for Lemon: 2

Please select cake size; Enter L for large, R for regular: l

Large Red Velvet Ingredient list:
Ingredient A:  25.1 Oz
Ingredient B:  25.1 Oz
Ingredient C:  26.9 Oz
Ingredient D:  20.0 Oz
Ingredient E:  14.9 Oz

Process finished with exit code 0

"""
