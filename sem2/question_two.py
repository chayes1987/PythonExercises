__author__ = 'Conor'

""" 2.
    a. Write a Python function that takes a string as an argument and returns the number of vowels in it. (12 marks)
    b. Explain the purpose of exceptions. When should you use them? (13 marks)
"""

# A.2 (a)
vowels = ['a', 'e', 'i', 'o', 'u']


# Function to count the number of vowels
def vowel_counter(string):
    total_vowels = 0
    for char in string:
        if char.lower() in vowels:
            total_vowels += 1
    return total_vowels

print(vowel_counter('hello'))
print(vowel_counter('iiiiii'))
print(vowel_counter('arsenal'))
print(vowel_counter('fhsdfhd'))

# A.2 (b)
# https://docs.oracle.com/javase/tutorial/essential/exceptions/definition.html
# Usually used for code which could act unexpectedly e.g. accessing a database, working with files, network code