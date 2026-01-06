"""
Write a program that computes the net amount of a bank account based a transaction log from console input. 
The transaction log format is shown as following:

D 100
W 200

D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100

Then, the output should be:
500

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
"""
balance = 0
while True:
    user_input = input()
    if user_input == "":
        break
    user_input = user_input.split()
    action = user_input[0]
    amount = user_input[1]
    if action == 'D':
        balance += int(amount)
    elif action == 'W':
        balance -= int(amount)
print(balance)