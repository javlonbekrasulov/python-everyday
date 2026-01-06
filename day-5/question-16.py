"""
Use a list comprehension to square each odd number in a list. 
The list is input by a sequence of comma-separated numbers. 
>Suppose the following input is supplied to the program:

1,2,3,4,5,6,7,8,9

Then, the output should be:

1,9,25,49,81

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
"""
#First solution 
user_input = input()
output = []

user_input = user_input.split(",")

for num in user_input:
    num = int(num)
    if num % 2 != 0:
        num = num*num
        output.append(str(num))
print(",".join(output))

#Solution using list comprehention
user_input = input().split(",")
output = [int(num)**2 for num in user_input if int(num)%2 != 0]
print(",".join(str(n) for n in output))