"""
File name: iterating_lists.py

Description: This snippet demonstrates: 4 different formats to iterate lists,
in conjunction with "for loop"
"""

# 1st format:
print("1st method of iteration; eg 1")
COLUMN_RANGE = 3
for row in [7,8,9]:
    print(row, '\t', end='')
print( )
print( )

# Or:
print("1st  method of iteration; eg 2")
sequence = [7, 8, 9]
for item in sequence:
    print(item, '\t', end='')
print( )
print( )

# 2nd format - iterator is the index:
print("2nd  method of iteration")
for idx in range(len(sequence)):
    print(sequence[idx], '\t', end='')
print( )
print( )

# 3nd format - both index and item value:
print("3rd  method of iteration")
for idx,item in enumerate(sequence):
    print("idx: ", idx, '\t', "item: ", item,'\t', end='')
print( )
print( )

# 4th format - items from multiple lists:
# eg 1
print("4th  method of iteration; eg 1")
new_sequence = [71, 81, 91]
item_numbers = [1, 2, 3]
for (line_number, new_item, item) in zip(item_numbers, new_sequence, sequence):
    print(line_number, ")", "dot product = ", new_item * item, '\t'*2, end='')
print( )
print( )

# eg 2
print("4th  method of iteration; eg 2")
LABEL_LST = ["Ingredient A: ", "Ingredient B: ","Ingredient C: "]
value_lst = [ 22, 10, 5]
for LABEL, ingredient in zip(LABEL_LST, value_lst):
    if ingredient != 0.0:  # print Only IF the wt is non-zero
        print(LABEL, ingredient)
