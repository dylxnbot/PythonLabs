"""
*******************************************************************************
Filename: make_more_cake_enhanced_sln.py
Author: Victor Lau
Date: 2019.02.18
Modifications: 2022.06.04
Description: This module performs the first stage of a cake making process.
It's tasks includes:
1) Query a cake order
2) Calculate the amounts, in oz, needed for each ingredient
3) print the ingredients list with the amounts for each
4) Repeat Step 1 - 3 until user enter 'q' or 'Q' to quit; a while
loop using sentinel
*******************************************************************************
"""




def print_ingrd(flour_wt,sugar_wt,unsweetened_cocoa_powder_wt,baking_powder_wt,
baking_soda_wt,salt_wt,egg_wt,buttermilk_wt,oil_wt,
vanilla_extract_wt,boiling_water_wt,red_food_coloring_wt,
distilled_vinegar_wt,butter_wt,sifted_self_rising_flour_wt,
fill_egg_yolk_wt,fill_sugar_wt,fill_butter_wt,
fill_lemon_zest_wt):
    """
    ***************************************************************************
    Function: print_ingrd( )
    Parameters: flour_wt # calculated weights of ingredient in oz
    sugar_wt
    unsweetened_cocoa_powder_wt
    baking_powder_wt
    baking_soda_wt
    salt_wt
    egg_wt
    buttermilk_wt
    oil_wt
    vanilla_extract_wt
    boiling_water_wt
    red_food_coloring_wt
    distilled_vinegar_wt
    butter_wt
    sifted_self_rising_flour_wt
    fill_egg_yolk_wt
    fill_sugar_wt
    fill_butter_wt
    fill_lemon_zest_wt
    Inputs: None
    Outputs: print the ingredients list with weight for each ingredient
    Returns: None
    Author: Victor Lau
    Date: 2019.02.18
    Modifications:
    Description:
    This function prints the ingredient list with each amount in oz. Tasks:
    1. Check the value of every parameter(possible ingredient)
    2. If the wt value is greater zero, print the ingredient name and its
    weight
    3. Calculate and print the total weight
    ***************************************************************************
    """
    if flour_wt != 0:
        print("%-28s%5.1f Oz" % ("Flour:", flour_wt))
    if sugar_wt != 0:
        print("%-28s%5.1f Oz" % ("Sugar: ", sugar_wt))
    if unsweetened_cocoa_powder_wt != 0:
        print("%-28s%5.1f Oz" % ("Unsweetened Cocoa Powder: ",unsweetened_cocoa_powder_wt))
    if baking_powder_wt != 0:
        print("%-28s%5.1f Oz" % ("Baking Powder: ",baking_powder_wt))
    if baking_soda_wt != 0:
        print("%-28s%5.1f Oz" % ("Baking Soda: ",baking_soda_wt))
    if salt_wt != 0:
        print("%-28s%5.1f Oz" % ("Salt: ",salt_wt))
    if egg_wt != 0:
        print("%-28s%5.1f Oz" % ("Egg: ",egg_wt))
    if buttermilk_wt != 0:
        print("%-28s%5.1f Oz" % ("Buttermilk: ",buttermilk_wt))
    if oil_wt != 0:
        print("%-28s%5.1f Oz" % ("Oil: ",oil_wt))
    if vanilla_extract_wt != 0:
        print("%-28s%5.1f Oz" % ("Vanilla Extract: ", vanilla_extract_wt))
    if boiling_water_wt != 0:
        print("%-28s%5.1f Oz" % ("Boiling Water: ", boiling_water_wt))
    if red_food_coloring_wt != 0:
        print("%-28s%5.1f Oz" % ("Red Food Coloring: ", red_food_coloring_wt))
    if distilled_vinegar_wt != 0:
        print("%-28s%5.1f Oz" % ("Distilled Vinegar: ", boiling_water_wt))
    if butter_wt != 0:
        print("%-28s%5.1f Oz" % ("Butter: ", boiling_water_wt))
    if sifted_self_rising_flour_wt != 0:
        print("%-28s%5.1f Oz" % ("Sifted Self Rising Flour: ",sifted_self_rising_flour_wt))

    # filling
    if fill_egg_yolk_wt != 0:
        print("%-28s%5.1f Oz" % ("Filling - Egg Yolk: ", fill_egg_yolk_wt))
    if fill_sugar_wt != 0:
        print("%-28s%5.1f Oz" % ("Filling - Sugar: ", fill_sugar_wt))
    if fill_butter_wt != 0:
        print("%-28s%5.1f Oz" % ("Filling - Butter: ", fill_butter_wt))
    if fill_lemon_zest_wt != 0:
        print("%-28s%5.1f Oz" % ("Filling - Lemon Zest: ", fill_lemon_zest_wt))

    # Verification - back calcuation to get total weight
    print("\n%-28s%5.1f Oz" % ("Total: ", flour_wt + sugar_wt + unsweetened_cocoa_powder_wt + baking_powder_wt + salt_wt +
                             egg_wt + butter_wt + oil_wt + vanilla_extract_wt + boiling_water_wt + red_food_coloring_wt
                             + distilled_vinegar_wt + butter_wt + sifted_self_rising_flour_wt + fill_egg_yolk_wt +
                             fill_sugar_wt + fill_butter_wt + fill_lemon_zest_wt + baking_soda_wt) )
    print()
    print()




def calc_n_print_chocolate_ingrd(cake_wt, size_label):
    """
    ***************************************************************************
    Function: calc_n_print_chocolate_ingrd( )
    Parameters: cake_wt - cake weight in oz
    size_label - either "Large" or "Regular"
    Inputs: None
    Outputs: 1. print the header indicating cake type and size
    2. print the ingredients list with weight for each ingredient;
    by calling print_ingrd( )
    Returns: None
    Author: Victor Lau
    Date: 2019.02.18
    Modifications:
    Description:
    This function calculates the weight of each ingredient for a
    Chocolate Cake according to the recipe. Tasks:
    1. Use constants to define the Chocolate Cake recipe
    2. Initialize all ingredient weights to zero
    3. Calculate the weights for each ingredient
    4. Print the Header and, Call print_ingrd( ) to print the ingredients list
    ***************************************************************************
    """
    # Chocolate cake recipe; in percentage of total weight
    CHOC_FLOUR_PCT = 15.8
    CHOC_SUGAR_PCT = 24.5
    CHOC_UNSWEETENED_COCOA_POWDER_PCT = 5.6
    CHOC_BAKING_POWER_PCT = 0.4
    CHOC_BAKING_SODA_PCT = 0.6
    CHOC_SALT_PCT = 0.4
    CHOC_EGG_PCT = 9.0
    CHOC_BUTTERMILK_PCT = 18.0
    CHOC_OIL_PCT = 8.1
    CHOC_VANILLA_EXTRACT_PCT = 0.6
    CHOC_BOILING_WATER_PCT = 17.0

    # zero every ingredient wt
    flour_wt = 0
    sugar_wt = 0
    unsweetened_cocoa_powder_wt = 0
    baking_powder_wt = 0
    baking_soda_wt = 0
    salt_wt = 0
    egg_wt = 0
    buttermilk_wt = 0
    oil_wt = 0
    vanilla_extract_wt = 0
    boiling_water_wt = 0
    red_food_coloring_wt = 0
    distilled_vinegar_wt = 0
    butter_wt = 0
    sifted_self_rising_flour_wt = 0

    # Filling
    fill_egg_yolk_wt = 0
    fill_sugar_wt = 0
    fill_butter_wt = 0
    fill_lemon_zest_wt = 0

    #calculate ingredient wts for chocolate cake
    flour_wt = cake_wt * CHOC_FLOUR_PCT/100
    sugar_wt = cake_wt * CHOC_SUGAR_PCT/100
    unsweetened_cocoa_powder_wt = cake_wt * CHOC_UNSWEETENED_COCOA_POWDER_PCT/100
    baking_powder_wt = cake_wt * CHOC_BAKING_POWER_PCT/100
    baking_soda_wt = cake_wt * CHOC_BAKING_SODA_PCT/100
    salt_wt = cake_wt * CHOC_SALT_PCT/100
    egg_wt = cake_wt * CHOC_EGG_PCT/100
    buttermilk_wt = cake_wt * CHOC_BUTTERMILK_PCT/100
    oil_wt = cake_wt * CHOC_OIL_PCT/100
    vanilla_extract_wt = cake_wt * CHOC_VANILLA_EXTRACT_PCT/100
    boiling_water_wt = cake_wt * CHOC_BOILING_WATER_PCT/100

    """
    ***************************************************************************
    OUTPUT
    ***************************************************************************
    """
    # First, print the header
    header = "%s Chocolate Cake Ingredient List\n" % (size_label)
    print(header)
    print_ingrd(flour_wt, sugar_wt, unsweetened_cocoa_powder_wt,
    baking_powder_wt, baking_soda_wt, salt_wt, egg_wt,
    buttermilk_wt, oil_wt, vanilla_extract_wt, boiling_water_wt,
    red_food_coloring_wt, distilled_vinegar_wt, butter_wt,
    sifted_self_rising_flour_wt, fill_egg_yolk_wt, fill_sugar_wt,
    fill_butter_wt, fill_lemon_zest_wt)




def calc_n_print_red_velvet_ingrd(cake_wt, size_label):
    """
    ***************************************************************************
    Function: calc_n_print_red_velvet_ingrd( )
    Parameters: cake_wt - cake weight in oz
    size_label - either "Large" or "Regular"
    Inputs: None
    Outputs: 1. print the header indicating cake type and size
    2. print the ingredients list with weight for each ingredient;
    by calling print_ingrd( )
    Returns: None
    Author: Victor Lau
    Date: 2019.02.18
    Modifications:
    Description:
    This function calculates the weight of each ingredient for a
    Red Velvet Cake according to the recipe. Tasks:
    1. Use constants to define the Chocolate Cake recipe
    2. Initialize all ingredient weights to zero
    3. Calculate the weights for each ingredient
    4. Print the Header and, Call print_ingrd( ) to print the ingredients list
    ***************************************************************************
    """
    # Red Velvet cake recipe; in percentage of total weight
    REDV_FLOUR_PCT = 22.4
    REDV_SUGAR_PCT = 22.4
    REDV_BAKING_SODA = 0.7
    REDV_SALT = 0.4
    REDV_UNSWEETENED_COCOA_POWDER = 0.4
    REDV_OIL = 24
    REDV_BUTTERMILK = 17.9
    REDV_EGG = 9
    REDV_RED_FOOD_COLORING = 2.1
    REDV_VANILLA_EXTRACT = 0.3
    REDV_DISTILLED_VINEGAR_PCT = 0.4

    # zero every ingredient wt
    flour_wt = 0
    sugar_wt = 0
    unsweetened_cocoa_powder_wt = 0
    baking_powder_wt = 0
    baking_soda_wt = 0
    salt_wt = 0
    egg_wt = 0
    buttermilk_wt = 0
    oil_wt = 0
    vanilla_extract_wt = 0
    boiling_water_wt = 0
    red_food_coloring_wt = 0
    distilled_vinegar_wt = 0
    butter_wt = 0
    sifted_self_rising_flour_wt = 0

    # Filling
    fill_egg_yolk_wt = 0
    fill_sugar_wt = 0
    fill_butter_wt = 0
    fill_lemon_zest_wt = 0

    # Calculate the ingredient wts for Red Velvet Cake
    flour_wt = cake_wt * REDV_FLOUR_PCT/100
    sugar_wt = cake_wt * REDV_SUGAR_PCT/100
    baking_soda_wt = cake_wt * REDV_BAKING_SODA/100
    salt_wt = cake_wt * REDV_SALT/100
    unsweetened_cocoa_powder_wt = cake_wt * REDV_UNSWEETENED_COCOA_POWDER/100
    oil_wt = cake_wt * REDV_OIL/100
    buttermilk_wt = cake_wt * REDV_BUTTERMILK/100
    egg_wt = cake_wt * REDV_EGG/100
    red_food_coloring_wt = cake_wt * REDV_RED_FOOD_COLORING/100
    vanilla_extract_wt = cake_wt * REDV_VANILLA_EXTRACT/100
    distilled_vinegar_wt = cake_wt * REDV_DISTILLED_VINEGAR_PCT/100

    """
    ***************************************************************************
    OUTPUT
    ***************************************************************************
    """
    # First, print the header
    header = "Ingredient Quantities for %s Red Velvet Cake" % (size_label)
    print(header)
    print_ingrd(flour_wt, sugar_wt, unsweetened_cocoa_powder_wt,
    baking_powder_wt, baking_soda_wt, salt_wt, egg_wt,
    buttermilk_wt, oil_wt, vanilla_extract_wt, boiling_water_wt,
    red_food_coloring_wt, distilled_vinegar_wt, butter_wt,
    sifted_self_rising_flour_wt, fill_egg_yolk_wt, fill_sugar_wt,
    fill_butter_wt, fill_lemon_zest_wt)
    # *****************************************************
    # End of calc_red_velvet_ingrd()
    # *****************************************************




def calc_n_print_lemon_ingrd(cake_wt, size_label):
    """
    ***************************************************************************
    Function: calc_n_print_lemon_ingrd( )
    Parameters: cake_wt - cake weight in oz
    size_label - either "Large" or "Regular"
    Inputs: None
    Outputs: 1. print the header indicating cake type and size
    2. print the ingredients list with weight for each ingredient;
    by calling print_ingrd( )
    Returns: None
    Author: Victor Lau
    Date: 2019.02.18
    Modifications:
    Description:
    This function calculates the weight of each ingredient for a
    Lemon Cake according to the recipe. Tasks:
    1. Use constants to define the Lemon Cake recipe
    2. Initialize all ingredient weights to zero
    3. Calculate the weights for each ingredient
    4. Print the Header and, Call print_ingrd( ) to print the ingredients list
    ***************************************************************************
    """
    # Lemon cake recipe; in percentage of total weight
    LEMO_BUTTER_PCT = 8.5
    LEMO_SUGAR_PCT = 15
    LEMO_EGG_PCT = 9
    LEMO_SIFTED_FLOUR = 15.6
    LEMO_BUTTERMILK_PCT = 9
    LEMO_VANILLA_EXTRACT = 0.2
    LEMO_FILL_EGG_YOLK_PCT = 17.9
    LEMO_FILL_SUGAR_PCT = 11.3
    LEMO_FILL_BUTTER_PCT = 2.1
    LEMO_FILL_LEMON_ZEST_PCT = 11.4

    # zero every ingredient wt
    flour_wt = 0
    sugar_wt = 0
    unsweetened_cocoa_powder_wt = 0
    baking_powder_wt = 0
    baking_soda_wt = 0
    salt_wt = 0
    egg_wt = 0
    buttermilk_wt = 0
    oil_wt = 0
    vanilla_extract_wt = 0
    boiling_water_wt = 0
    red_food_coloring_wt = 0
    distilled_vinegar_wt = 0
    butter_wt = 0
    sifted_self_rising_flour_wt = 0

    # Filling
    fill_egg_yolk_wt = 0
    fill_sugar_wt = 0
    fill_butter_wt = 0
    fill_lemon_zest_wt = 0

    # Calculate the ingredient wts for Lemon Cake
    butter_wt = cake_wt * LEMO_BUTTER_PCT/100
    sugar_wt = cake_wt * LEMO_SUGAR_PCT/100
    egg_wt = cake_wt * LEMO_EGG_PCT/100
    sifted_self_rising_flour_wt = cake_wt * LEMO_SIFTED_FLOUR/100
    buttermilk_wt = cake_wt * LEMO_BUTTERMILK_PCT/100
    vanilla_extract_wt = cake_wt * LEMO_VANILLA_EXTRACT/100
    fill_egg_yolk_wt = cake_wt * LEMO_FILL_EGG_YOLK_PCT/100
    fill_sugar_wt = cake_wt * LEMO_FILL_SUGAR_PCT/100
    fill_butter_wt = cake_wt * LEMO_FILL_BUTTER_PCT/100
    fill_lemon_zest_wt = cake_wt * LEMO_FILL_LEMON_ZEST_PCT/100

    """
    ***************************************************************************
    OUTPUT
    ***************************************************************************
    """
    # First, print the header
    header = "Ingredient Quantities for %s Lemon Cake" % (size_label)
    print(header)
    print_ingrd(flour_wt, sugar_wt, unsweetened_cocoa_powder_wt,
    baking_powder_wt, baking_soda_wt, salt_wt, egg_wt,
    buttermilk_wt, oil_wt, vanilla_extract_wt, boiling_water_wt,
    red_food_coloring_wt, distilled_vinegar_wt, butter_wt,
    sifted_self_rising_flour_wt, fill_egg_yolk_wt, fill_sugar_wt,
    fill_butter_wt, fill_lemon_zest_wt)
    # *****************************************************
    # End of calc_lemon_ingrd()
    # *****************************************************




def make_cake_loop():
    """
    ***************************************************************************
    Function: make_cake_loop( )
    Parameters: None
    Inputs: cake_type 1 - Chocolate; 2 - Red Velvet; 3 - Lemon;
    cake_size 'L' - Large; 'R' - Regular
    Outputs: print the ingredients list with weight for each ingredient
    Returns: None
    Author: Victor Lau
    Date: 2019.02.18
    Modifications:
    Description:
    This function is effectively the whole main program. It contains:
    1. All three recipes; Chocolate, Red Velvet and Lemon
    2. Initialization of all variables
    3. Query the cake order
    4. Calculate the ingredients amounts for the cake just order
    5. Print the ingredient list accompanied by weights
    6. Repeat Step 3 - 5 until user enter 'q' or 'Q' to quit
    ***************************************************************************
    """
    # Cake size - weight in oz
    LARGE_CAKE_WT = 7 * 16
    REGULAR_CAKE_WT = 4 * 16
    cake_wt = 0

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
        # query cake size
        cake_type = eval(cake_type_raw)
        cake_size = input("Please Select Cake Size; Enter L for large, R for regular: ")
        print()

        #Determine cake_wt and size_label
        if cake_size == 'R' or cake_size == 'r':
            cake_wt = REGULAR_CAKE_WT
            size_label = "Regular"
        elif cake_size == 'L' or cake_size == 'l':
            cake_wt = LARGE_CAKE_WT
            size_label = "Large"

        # if the cake selected is Chocolate Cake
        if cake_type == 1:
            if cake_size == 'R' or cake_size == 'r':
                cake_wt = REGULAR_CAKE_WT
                size_label = "Regular"
            elif cake_size == 'L' or cake_size == 'l':
                cake_wt = LARGE_CAKE_WT
                size_label = "Large"
            calc_n_print_chocolate_ingrd(cake_wt, size_label)

        # if cake selected is Red Velvet
        elif cake_type == 2:
            if cake_size == 'R' or cake_size == 'r':
                cake_wt = REGULAR_CAKE_WT
                size_label = "Regular"
            elif cake_size == 'L' or cake_size == 'l':
                cake_wt = LARGE_CAKE_WT
                size_label = "Large"
            calc_n_print_red_velvet_ingrd(cake_wt, size_label)

        # if the cake selected is Lemon Cake
        else:
            if cake_size == 'R' or cake_size == 'r':
                cake_wt = REGULAR_CAKE_WT
                size_label = "Regular"
            elif cake_size == 'L' or cake_size == 'l':
                cake_wt = LARGE_CAKE_WT
                size_label = "Large"
            calc_n_print_lemon_ingrd(cake_wt, size_label)

        # take next order - query cake type; if 'q' or 'Q' was entered then quit the program
        cake_type_raw = input("Please Select Cake Type; Enter 1 for Chocolate, 2 for Red Velvet, 3 for Lemon, q to quit: ")

    # *************************************************************************
    # end of while loop
    # *************************************************************************
    print("Bye")




'''
*******************************************************************************
Program Starts Here
*******************************************************************************
'''
make_cake_loop()




"""
This is the record of execution

C:\PycharmProjects\.venv\Scripts\python.exe C:\PycharmProjects\pythonProject\lab7test.py 
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