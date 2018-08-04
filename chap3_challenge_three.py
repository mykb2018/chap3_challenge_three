# Write a program that prints a message if a variable is less than or equal to 10,
# another message if the variable is greater than 10 but less than or equal to 25,
# and another message if the variable is greater than 25.

from random import *

x = randint(1, 50)

if x <= 10:
    print("Number is " + str(x) + " and it is less than or equal to 10.")
elif x > 10 and x <= 25:
    print("Number is " + str(x) + " and it is greater than 10 but less than or equal to 25.")
else:
    print("Number is " + str(x) + " and it is greater than 25.")