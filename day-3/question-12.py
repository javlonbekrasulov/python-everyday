"""
Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
"""

output = []

for number in range(1000, 3001):
    number = str(number)
    all_even = True

    for n in number:
        if int(n) % 2 != 0:
            all_even = False
            break
    if all_even:
        output.append(number)

print(",".join(output))