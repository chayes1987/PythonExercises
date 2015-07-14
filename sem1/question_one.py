__author__ = 'Conor'

"""
Q.1 Write a Python program that reads in 9 assignment marks from a user and displays the average of the 9 assignments.
    The assignments are marked out of 10 and the overall result should be a percentage. A sample of the program running:

    Enter mark for assignment 1: 4
    Enter mark for assignment 2: 7
    …
    Enter mark for assignment 9: 6

    Overall result = 54.17%

    (25 marks)
"""

# A.1 without validation

# Initialize some variables
total = 0
max_mark = 10

# Create loop for the 9 inputs
for num in range(1, 10):
    # Read in and add to the total
    mark = input('Enter mark for assignment %s: ' % num)
    total += int(mark)

# Print the average
print('Overall result = %s%%' % round(total / num * max_mark, 2))


# A.1 with validation
total = 0
max_mark = 10

for num in range(1, 10):
    # Take input and assume it is invalid
    mark = input('Enter mark for assignment %s: ' % num)
    invalid = True
    # Check for blanks, non-integers, and integers > 10
    while invalid:
        if '' == mark:
            print('Mark must not be blank')
            mark = input('Enter mark for assignment %s: ' % num)
        elif not mark.isdigit():
            print('Mark must be an integer')
            mark = input('Enter mark for assignment %s: ' % num)
        elif int(mark) > max_mark:
            print('Mark must be less than %s' % max_mark)
            mark = input('Enter mark for assignment %s: ' % num)
        else:
            # Jump out of the loop
            invalid = False

    # Add to the total
    total += int(mark)

# Print the average
print('Overall result = %s%%' % round(total / num * max_mark, 2))