__author__ = 'Conor'

"""
Q.2 Write a Python program that reads in a month of the year from the user and prints out the name of the next month.
    A sample of the program running:

    Enter a month: March Next month is April

    Your code should work for all 12 months.

    (25 marks)
"""

# A.2

# Initialize a list of the months of the year
months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august',
          'september', 'october', 'november', 'december']

# Get the input from the user and assume it is invalid
month = input('Enter a month: ')
invalid = True

while invalid:
    # See if the input is in the list
    if not month.lower() in months:
        # It isn't, ask for it again
        print('%s is not a valid month' % month)
        month = input('Enter a month: ')
    else:
        # It is, jump out of the loop
        invalid = False

# Check for December and set index to January
if 'december' == month.lower():
    index = 0
else:
    # Otherwise set index to current month + 1 position
    index = months.index(month.lower()) + 1

# Print the output (title() function will capitalize the first letter)
print('%s Next month is %s' % (month, months[index].title()))