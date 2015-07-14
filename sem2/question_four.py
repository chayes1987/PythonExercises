__author__ = 'Conor'

""" 4.
    a. Write a Python program that asks the user to enter the name of a file and then prints out the contents of the
        file. If the file does not exist you should print a message saying so. (10 marks)
    b. Write a Python program that reads in the name, exam mark and assessment mark for 50 students. Your program
        should then print out the name and average mark of the student who had the highest average exam/assessment
        mark. (15 marks)
"""

# A.4 (a)

# Create file c:\helloworld.txt with contents 'Hello World!'
name_of_file = input('Enter the name of your file: ')

# Try block to catch exceptions e.g. File doesn't exist
try:
    # Read file
    my_file = open(name_of_file)
    # Show contents
    print(my_file.read())
except FileNotFoundError:
    print('File \'%s\' does not exist.' % name_of_file)
    pass

# A.4 (b)

# Initialize empty list of students
students = []


# Student class
class Student:

    # Constructor to set properties
    def __init__(self, forename, mark):
        self.name = forename
        self.average_mark = mark


# 50 too many, this is for 2
for student in range(0, 2):
    # Read in fields
    name = input('Enter name: ')
    exam_mark = input('Enter exam mark: ')
    assessment_mark = input('Enter assessment mark: ')
    # Create student instance
    average_mark = (float(exam_mark) + float(assessment_mark)) / 2
    student = Student(name, average_mark)
    # Add to the list
    students.append(student)

# Default the first student as the highest
highest_stud = students[0]

for stud in students:
    if stud.average_mark > highest_stud.average_mark:
        highest_stud = stud

print('\nName: %s \nAverage Mark: %s%%' % (highest_stud.name, highest_stud.average_mark))