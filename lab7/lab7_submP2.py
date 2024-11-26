"""
*******************************************************************************
Filename: lab7_subm.py

Author: Dylan Lam

Date: 11/25/2024

Modifications: 11/25/2024

Description: This module performs the first stage of a cake making process.

It's tasks includes:
1) Query a cake order
2) Calculate the amounts, in oz, needed for each ingredient
3) print the ingredients list with the amounts for each
4) Repeat Step 1 - 3 until user enter 'q' or 'Q' to quit; a while
loop using sentinel
*******************************************************************************
"""



def print_ingrd(ck_label, size_label, wt_list, LABEL_LIST):
    """
    ***************************************************************************

    Function: print_ingrd(ck_label, size_label, wt_list, LABEL_LIST)

    Parameters: ck_label - the type of cake
                size_label - the size of the cake
                wt_list - the list of ingredient weights
                LABEL_LIST - the list of ingredient names corresponding to the weights

    Outputs: Lists the cake size, type of cake, and ingredients

    Returns: None

    Author: Dylan Lam

    Date: 11/25/2024

    Modifications: 11/25/2024

    Description:
    This function takes in four parameters, cake type, cake size, the list of ingredients, and the list of
    ingredient names. It then outputs the cake type, size, and amount of each ingredient used along with the total
    amount of ingredients used.

    ***************************************************************************
    """
    """
    ***************************************************************************
    OUTPUT
    ***************************************************************************
    """
    print()
    header = f"{size_label} {ck_label} Cake Ingredient List\n"
    print(header)
    total_weight = 0
    for label, weight in zip(LABEL_LIST, wt_list):
        if weight > 0:
            print(f"{label:<28} {weight:5.1f} Oz")
            total_weight += weight
    print()
    print(f"{'Total:':<28} {total_weight:5.1f} Oz\n\n")



def calc_ingrd(cake_wt, recipe):
    """
    ***************************************************************************

    Function: calc_ingrd(cake_wt, recipe)

    Parameters: cake_wt - the weight of the cake in ounces
                recipe - a dictionary with ingredient names as keys and percentages as values

    Outputs: None

    Returns: A list of calculated weights corresponding to the ingredient names.

    Author: Dylan Lam

    Date: 11/25/2024

    Modifications: 11/25/2024

    Description:
    This function takes in two parameters, cake weight and the recipe. It then returns a list of calculated
    ingredients corresponding to the ingredient name.

    ***************************************************************************
    """
    return [cake_wt * percentage / 100 for percentage in recipe.values()]



def make_cake_loop():
    """
    ***************************************************************************

    Function: make_cake_loop()

    Parameters: None

    Outputs: Prints the ingredients and their weights for the selected cake type and size.

    Returns: None

    Author: Dylan Lam

    Date: 11/25/2024

    Modifications: 11/25/2024

    Description:
    This function provides a user interface to select a cake type and size. Based on the user input, it calculates
    the ingredient weights using the appropriate recipe and outputs the results. The user can choose between three cake
    types and two sizes. The loop continues until the user quits.

    ***************************************************************************
    """

    # Cake size - weight in oz
    LARGE_CAKE_WT = 7 * 16
    REGULAR_CAKE_WT = 4 * 16

    # Recipes as dictionaries
    recipes = {
        "Chocolate": {
            "Flour": 15.8,
            "Sugar": 24.5,
            "Unsweetened Cocoa Powder": 5.6,
            "Baking Powder": 0.4,
            "Baking Soda": 0.6,
            "Salt": 0.4,
            "Egg": 9.0,
            "Buttermilk": 18.0,
            "Oil": 8.1,
            "Vanilla Extract": 0.6,
            "Boiling Water": 17.0
        },
        "Red Velvet": {
            "Flour": 22.4,
            "Sugar": 22.4,
            "Baking Soda": 0.7,
            "Salt": 0.4,
            "Unsweetened Cocoa Powder": 0.4,
            "Oil": 24.0,
            "Buttermilk": 17.9,
            "Egg": 9.0,
            "Red Food Coloring": 2.1,
            "Vanilla Extract": 0.3,
            "Distilled Vinegar": 0.4
        },
        "Lemon": {
            "Butter": 8.5,
            "Sugar": 15.0,
            "Egg": 9.0,
            "Sifted Self Rising Flour": 15.6,
            "Buttermilk": 9.0,
            "Vanilla Extract": 0.2,
            "Filling - Egg Yolk": 17.9,
            "Filling - Sugar": 11.3,
            "Filling - Butter": 2.1,
            "Filling - Lemon Zest": 11.4
        }
    }

    # Common ingredient names list
    INGRD_NAME_LIST = [
        "Flour", "Sugar", "Unsweetened Cocoa Powder", "Baking Powder", "Baking Soda",
        "Salt", "Egg", "Buttermilk", "Oil", "Vanilla Extract", "Boiling Water",
        "Red Food Coloring", "Distilled Vinegar", "Butter", "Sifted Self Rising Flour",
        "Filling - Egg Yolk", "Filling - Sugar", "Filling - Butter", "Filling - Lemon Zest"
    ]


    """
    *******************************************************************************
    INPUT
    *******************************************************************************
    """
    # query cake type; if 'q' or 'Q' was entered then quit the program
    cake_type_raw = input("Please Select Cake Type; Enter 1 for Chocolate, 2 for Red Velvet, 3 for Lemon, q to quit: ")

    # *************************************************************************
    # Sentinel to take cake order input
    # *************************************************************************
    while not(cake_type_raw == 'q' or cake_type_raw == 'Q'):

        # Choosing cake type
        if cake_type_raw == '1':
            recipe_name = "Chocolate"
        elif cake_type_raw == '2':
            recipe_name = "Red Velvet"
        elif cake_type_raw == '3':
            recipe_name = "Lemon"
        else:
            print("Invalid selection. Try again.")
            continue

        # Query cake size
        cake_size = input("Please Select Cake Size; Enter L for large, R for regular: ").lower()
        if cake_size == 'r':
            cake_wt = REGULAR_CAKE_WT
            size_label = "Regular"
        elif cake_size == 'l':
            cake_wt = LARGE_CAKE_WT
            size_label = "Large"
        else:
            print("Invalid size selection. Try again.")
            continue

        # Calculate the ingredients
        recipe = recipes[recipe_name]
        ingrd_list = calc_ingrd(cake_wt, recipe)

        # Output the results
        print_ingrd(recipe_name, size_label, ingrd_list, list(recipe.keys()))

        # Prompt for the next cake type
        cake_type_raw = input("Please Select Cake Type; Enter 1 for Chocolate, 2 for Red Velvet, 3 for Lemon, q to quit: ")
    # *************************************************************************
    # end of while loop
    # *************************************************************************
    print("Bye!")



'''
*******************************************************************************
Program Starts Here
*******************************************************************************
'''
make_cake_loop()



"""
This is the record of execution

C:\\PycharmProjects\\.venv\\Scripts\\python.exe C:\\PycharmProjects\\pythonProject\\lab7test.py 
Please Select Cake Type; Enter 1 for Chocolate, 2 for Red Velvet, 3 for Lemon, q to quit: 2
Please Select Cake Size; Enter L for large, R for regular: l

Large Red Velvet Cake Ingredient List

Flour                         25.1 Oz
Sugar                         25.1 Oz
Baking Soda                    0.8 Oz
Salt                           0.4 Oz
Unsweetened Cocoa Powder       0.4 Oz
Oil                           26.9 Oz
Buttermilk                    20.0 Oz
Egg                           10.1 Oz
Red Food Coloring              2.4 Oz
Vanilla Extract                0.3 Oz
Distilled Vinegar              0.4 Oz

Total:                       112.0 Oz


Please Select Cake Type; Enter 1 for Chocolate, 2 for Red Velvet, 3 for Lemon, q to quit: 3
Please Select Cake Size; Enter L for large, R for regular: r

Regular Lemon Cake Ingredient List

Butter                         5.4 Oz
Sugar                          9.6 Oz
Egg                            5.8 Oz
Sifted Self Rising Flour      10.0 Oz
Buttermilk                     5.8 Oz
Vanilla Extract                0.1 Oz
Filling - Egg Yolk            11.5 Oz
Filling - Sugar                7.2 Oz
Filling - Butter               1.3 Oz
Filling - Lemon Zest           7.3 Oz

Total:                        64.0 Oz


Please Select Cake Type; Enter 1 for Chocolate, 2 for Red Velvet, 3 for Lemon, q to quit: 3
Please Select Cake Size; Enter L for large, R for regular: l

Large Lemon Cake Ingredient List

Butter                         9.5 Oz
Sugar                         16.8 Oz
Egg                           10.1 Oz
Sifted Self Rising Flour      17.5 Oz
Buttermilk                    10.1 Oz
Vanilla Extract                0.2 Oz
Filling - Egg Yolk            20.0 Oz
Filling - Sugar               12.7 Oz
Filling - Butter               2.4 Oz
Filling - Lemon Zest          12.8 Oz

Total:                       112.0 Oz


Please Select Cake Type; Enter 1 for Chocolate, 2 for Red Velvet, 3 for Lemon, q to quit: 1
Please Select Cake Size; Enter L for large, R for regular: r

Regular Chocolate Cake Ingredient List

Flour                         10.1 Oz
Sugar                         15.7 Oz
Unsweetened Cocoa Powder       3.6 Oz
Baking Powder                  0.3 Oz
Baking Soda                    0.4 Oz
Salt                           0.3 Oz
Egg                            5.8 Oz
Buttermilk                    11.5 Oz
Oil                            5.2 Oz
Vanilla Extract                0.4 Oz
Boiling Water                 10.9 Oz

Total:                        64.0 Oz


Please Select Cake Type; Enter 1 for Chocolate, 2 for Red Velvet, 3 for Lemon, q to quit: 2
Please Select Cake Size; Enter L for large, R for regular: r

Regular Red Velvet Cake Ingredient List

Flour                         14.3 Oz
Sugar                         14.3 Oz
Baking Soda                    0.4 Oz
Salt                           0.3 Oz
Unsweetened Cocoa Powder       0.3 Oz
Oil                           15.4 Oz
Buttermilk                    11.5 Oz
Egg                            5.8 Oz
Red Food Coloring              1.3 Oz
Vanilla Extract                0.2 Oz
Distilled Vinegar              0.3 Oz

Total:                        64.0 Oz


Please Select Cake Type; Enter 1 for Chocolate, 2 for Red Velvet, 3 for Lemon, q to quit: 1
Please Select Cake Size; Enter L for large, R for regular: l

Large Chocolate Cake Ingredient List

Flour                         17.7 Oz
Sugar                         27.4 Oz
Unsweetened Cocoa Powder       6.3 Oz
Baking Powder                  0.4 Oz
Baking Soda                    0.7 Oz
Salt                           0.4 Oz
Egg                           10.1 Oz
Buttermilk                    20.2 Oz
Oil                            9.1 Oz
Vanilla Extract                0.7 Oz
Boiling Water                 19.0 Oz

Total:                       112.0 Oz


Please Select Cake Type; Enter 1 for Chocolate, 2 for Red Velvet, 3 for Lemon, q to quit: q
Bye!

Process finished with exit code 0
"""