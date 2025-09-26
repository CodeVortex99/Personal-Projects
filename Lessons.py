#Array:
# Type of List - Contains items of the same data type.

# 1d Array

text = input('Enter text: ').strip() # Removes white spaces on the front and back.
text = input('Enter text: ').split() # Converts into a list with words as elements.

text = input('Enter text: ')
TextL = list(text) #Converts the text into list where each character is the element.

fruits = ['mango', 'apple', 'banana', 'orange']
# The items of the array can be accessed through their index positions.
# Python follows 0-index system.

# 2D Array

Objects = [['Mango', 'Banana', 'Apple'], ['Pencil', 'Pen', 'Eraser']] # A 2D array contains of items which are in the form of lists.

#Sub-routine

NUm = int(input('Enter a num: '))
Num = int(input('Enter a num: '))

def add(num1, num2):
    Sum = num1 + num2
    return Sum

Sum1 = add(NUm, Num)
print(Sum1) # Used for reusability.

#Functions
# - Returns a value, TO call a function, it is used as part of a sentence.

#Procedure
# - Doesn't return a value.
# - print statements

#Parameters:
# - Holds information on the data required by the subroutine.

# Arguments: Nicknames for parameters
# - The data passed into the sub-routine.