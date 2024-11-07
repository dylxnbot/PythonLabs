"""
***************************************************************************
Filename:      lab3_subm.py

Author:        Dylan Lam

Date:          10/16/2024

Modifications: Dylan – 10/16/2024

Description:   This module demonstrates the use of functions to:
               1) perform indentation
               2) center a string on the screen

***************************************************************************
"""


"""
***************************************************************************

Function: indent( string, spaces )

Parameters: string - string to be printed
            spaces - number of spaces to be indented for printing

Outputs: print the string with indentation specified by "spaces"

Returns: None

Author: Dylan Lam

Date: 10/16/2024

Modifications: 10/16/2024

Description:
This function prints a string with a specified number of white spaces indented.
The first parameter is a string literal or variable.
The second parameter is the number of white space to be indented.

***************************************************************************
"""
def indent(string, spaces):
    print(' ' * spaces + string)


"""
***************************************************************************

Function: center(user_text, screen_width)

Parameters: user_text - text that will be counted
            screen_width - width of the screen given by user
            length - counts the number of characters from user_text
            center_screen - finds the center of the screen by dividing screen_width by 2
            indentation - how many indents are needed before printing the text

Outputs: None

Returns: The number of white spaces indented before the text is printed

Author: Dylan Lam

Date: 10/16/2024

Modifications: 10/16/2024

Description:
This function centers a string with respect to the screen width.
The first parameter is a string literal or variable.
The second parameter is the width of the screen.
The third parameter is the character length of the user_text.
The fourth paramater finds the center of the screen by dividing screen_width by 2.
The fifth parameter is going to be the number of white spaces printed before the text.

***************************************************************************
"""
def center(user_text, screen_width):
    length = len(user_text)                 #counting the number of characters in the text
    center_screen = int(screen_width/2)     #needs int() otherwise would be float
    indentation = center_screen - length
    indent(user_text, indentation)
    return indentation


"""
***************************************************************************

Function: read_center_text()

Parameters: input_text - prompts user to enter a string
            input_screen - prompts user to enter the width of the screen
            indents - assigns return of center() function to the parameter

Outputs: Prompt asking for user to enter a string literal.
         Prompt asking for user to enter screen width.
         Prints the number of indents to the console.

Returns: None

Author: Dylan Lam

Date: 10/16/2024

Modifications: 10/16/2024

Description:
This function interacts with the user to print text strings that are centered.
The first parameter is a string literal.
The second parameter is an int variable.
The third parameter is a variable that contains the return value of the center() function.

***************************************************************************
"""
def read_center_text():
    input_text = input("Enter Text String: ")
    input_screen = int(input("Enter Screen Width: "))
    indents = center(input_text, input_screen)
    print("Indented by %d white spaces" % indents)


#Main
read_center_text()


"""
This is the record of execution

C:\PycharmProjects\.venv\Scripts\python.exe C:\PycharmProjects\pythonProject\lab3_subm.py 
Enter Text String: hello there
Enter Screen Width: 40
         hello there
Indented by 9 white spaces

Process finished with exit code 0
"""