import random

lower_input = int(input("Enter the lower bound integer: "))
upper_input = int(input("Enter the upper bound integer: "))

random_number = random.randrange(lower_input, upper_input)

print(random_number)