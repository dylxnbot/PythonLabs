"""
CIS 40 Lab 2.2 Problem 2- The Price of Books

Suppose the cover price of a book is $24.95, but bookstores get a 40% discount.
Shipping costs $3 for the first copy and 75 cents for each additional copy.
What is the total wholesale cost for 60 copies?
"""

bookPrice = float(input("Enter the price of the book: ")) * .4  #Price of a book at wholesale price
numBooks = int(input("Enter the number of books: "))

numBookPrice = bookPrice * numBooks
shipPrice = 3 + ((numBooks-1) * .75)
totPrice = numBookPrice + shipPrice

print('\nThe total cost for %d books is: %.2f' % (numBooks, totPrice))

"""
This is the record of execution

C:\PycharmProjects\.venv\Scripts\python.exe C:\PycharmProjects\pythonProject\lab2_subm.py 
Enter the price of the book: 24.95
Enter the number of books: 60

The total cost for 60 books is: 646.05

Process finished with exit code 0
"""