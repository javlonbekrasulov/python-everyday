"""
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program: 8 
Then, the output should be:40320
"""



num = int(input("Enter the number:"))

factorial = 1

i = 1

#using while loop
while i <= num:
    factorial = factorial * i;
    i = i + 1
print(f"Answer is: {factorial}")

#using for loop
for i in range(i, num + 1):
    factorial = factorial * i;
print(f"Answer is: {factorial}")