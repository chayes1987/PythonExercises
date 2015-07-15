__author__ = 'Conor'

""" 3.
    a. Write a Python program that reads 10 numbers into a list and then sorts the list into ascending order. (12 marks)
    b. Write a function that takes a list as its argument and prints out only the elements at
        odd positions (1,3,5, etc.). (13 marks)
"""

# A.3 (a)

# Initialize empty list
numbers = []

# Read in the 10 numbers
for num in range(0, 10):
    number = input('Enter a number: ')
    numbers.append(int(number))

# Sort and print
numbers.sort()
print(numbers)

# A.3 (b)


# Function prints elements in odd positions
def i_print_odd_elements(elements):
    # elements[0::2] -> 0 represents where to begin, the middle is blank meaning the whole length, 2 is the step
    print(elements[0::2])

i_print_odd_elements([1, 2, 3, 4])
i_print_odd_elements(['Hello', '', 'World', ''])
