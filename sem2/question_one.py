__author__ = 'Conor'

""" 1.
    a. Write a Python program that generates 10 random numbers between 1 and 100 (inclusive) and calculates and
        displays the average of the generated numbers.
        (12 marks)
    b. Write a function that takes 3 numbers as arguments and returns the value of the largest of the 3 numbers.
        (13 marks)
"""

# A.1 (a)

# Import required package
from random import randint

# Initialize required variables
min_num = 1
max_num = 100
total = 0

# Loop runs 10 times
for num in range(1, 11):
    # Generate random number
    random_num = randint(min_num, max_num)
    print('Random number %s: %s' % (num, random_num))
    # Add to total for calculation after
    total += random_num

# Print the average
print('Average: %s' % (total/10))

# A.1 (b)


# Fast way
def max_num(num_one, num_two, num_three):
    return max(num_one, num_two, num_three)

# Call the function
print(max_num(1, 2, 3))


# Alternative
def my_max_num(num_one, num_two, num_three):
    maximum_num = num_one

    if num_two > maximum_num:
        maximum_num = num_two
    if num_three > maximum_num:
        maximum_num = num_three

    return maximum_num

# Call the function
print(my_max_num(4, 1, 6))

