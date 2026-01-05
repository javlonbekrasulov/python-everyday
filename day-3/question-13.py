"""
Write a program that accepts a sentence and calculate the number of letters and digits.

Suppose the following input is supplied to the program:

hello world! 123
Then, the output should be:

LETTERS 10
DIGITS 3
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input
"""

user_input = input()
letter_count = 0
number_count = 0

for character in user_input:
    if character.isalpha():
        letter_count += 1
    if character.isdigit():
        number_count += 1
print(f"LETTERS {letter_count}\nDIGITS {number_count}")

