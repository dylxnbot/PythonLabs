"""
*******************************************************************************
Filename: lab8_subm.py

Author: Dylan Lam

Date: 11/30/2024

Modifications: 12/3/2024

Description:
This function creates and prints 6 cake objects with different flavors and sizes. Based on the object's flavors and size,
it calculates the ingredient weights using the appropriate recipe and outputs the results.
***********************************************************************
"""


class Cake:
    """
    Cake class - A class to represent a cake with various types and sizes. Calculates ingredient quantities accordingly.

    Parameters:
    type - (int) Represents the type of the cake (1 for Chocolate, 2 for Red Velvet, 3 for Lemon).
    size - (str) Represents the size of the cake ('R' for Regular, 'L' for Large).
    name - (str) The name of the cake based on the selected type.
    weight - (float) The weight of the cake in ounces.
    recipe - (dict) A dictionary of ingredient labels and percentages for the cake.
    ingrd_list - (list) A nested list representing ingredient labels and corresponding weights.

    Methods:
    __init__(self, type, size) - Initializes a Cake object with a specific type and size, sets name, weight, and calculates ingredients.
    calc_ingrd(self, weight, recipe) - Calculates the ingredient weights based on the cake weight and recipe percentages.
    __str__(self) - Returns a formatted string listing the ingredients and their quantities for the cake.

    Author: Dylan Lam

    Date: 11/30/2024

    Modifications: 12/3/2024

    Description:
    The Cake class represents three different types of cakes that can be made in two different sizes.
    Each cake object is initialized with parameters type, size, name, weight, and a recipe.
    """


    def __init__(self, type, size):
        """
        ***************************************************************************

        Function: __init__(self, type, size)

        Parameters: type - the type of cake, chocolate, red velvet, or lemon
                    size - the size of the cake, regular or large

        Outputs: None

        Returns: None

        Author: Dylan Lam

        Date: 11/30/2024

        Modifications: 12/3/2024

        Description:
        This function takes in two parameters, the type and size of the cake object. Sets the name of the cake object
        based on the cake type and size.

        ***************************************************************************
        """
        self.type = type
        self.size = size

        # Set the name and weight based on cake type and size
        if self.type == 1:
            self.name = "Chocolate"
            self.recipe = {
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
            }
        elif self.type == 2:
            self.name = "Red Velvet"
            self.recipe = {
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
            }
        elif self.type == 3:
            self.name = "Lemon"
            self.recipe = {
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

        # Set the weight based on size
        if self.size == 'L':
            self.weight = 112  # Large Cake Weight
            self.cake_size = "Large"
        elif self.size == 'R':
            self.weight = 64  # Regular Cake Weight
            self.cake_size = "Regular"

        # Calculate the ingredients list
        self.calc_ingrd(self.weight, self.recipe)

    def calc_ingrd(self, weight, recipe):
        """
        ***************************************************************************

        Function: calc_ingrd(self, weight, recipe)

        Parameters: weight - the weight of the cake, regular is 64oz and large is 112oz
                    recipe - the weight of each ingredient according to the type of cake

        Outputs: None

        Returns: None

        Author: Dylan Lam

        Date: 11/30/2024

        Modifications: 12/3/2024

        Description:
        This function takes in two parameters, the weight and recipe of the cake. Based on the weight of the cake object,
        the function sets the weight of the object to 64 or 112 ounces. It then uses the weight of the object to
        calculate the amount of each ingredient in the cake object.

        ***************************************************************************
        """
        ingredient_labels = list(recipe.keys())
        ingredient_weights = [weight * percentage / 100 for percentage in recipe.values()]
        self.ingrd_list = [ingredient_labels, ingredient_weights]

    def __str__(self):
        """
        ***************************************************************************

        Function: __str__(self)

        Parameters: None

        Outputs: None

        Returns: A string with the size and name of the cake, and a list of the weight of every ingredient of the cake.

        Author: Dylan Lam

        Date: 11/30/2024

        Modifications: 12/3/2024

        Description:
        This function takes in no parameters. FINSIH THIS DECRIPTIONFINSIH THIS DECRIPTIONFINSIH THIS DECRIPTIONFINSIH THIS DECRIPTIONFINSIH THIS DECRIPTIONFINSIH THIS DECRIPTIONFINSIH THIS DECRIPTIONFINSIH THIS DECRIPTIONFINSIH THIS DECRIPTIONFINSIH THIS DECRIPTIONFINSIH THIS DECRIPTION
        ***************************************************************************
        """
        cake_string = f"Ingredient Quantities for {self.cake_size} {self.name} Cake\n"
        cake_string += "\n"
        for ingrd_label, ingrd_wt in zip(self.ingrd_list[0], self.ingrd_list[1]):
            if ingrd_wt > 0:
                cake_string += f"{ingrd_label:<28} {ingrd_wt:5.1f} Oz\n"
        cake_string += "\n"
        return cake_string


""" 
**********************************************
        Create and print cake objects 
**********************************************
"""
reg_chocolate_cake = Cake(1, 'R')
lrg_chocolate_cake = Cake(1, 'L')
reg_red_velvet_cake = Cake(2, 'R')
lrg_red_velvet_cake = Cake(2, 'L')
reg_lemon_cake = Cake(3, 'R')
lrg_lemon_cake = Cake(3, 'L')

print(reg_chocolate_cake)
print(lrg_chocolate_cake)
print(reg_red_velvet_cake)
print(lrg_red_velvet_cake)
print(reg_lemon_cake)
print(lrg_lemon_cake)
