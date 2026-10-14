import random

numbers = []

#ask how many number do you want to add
#append ramdomly numbers to the list
amount = int(input("how many numbers do you want to add:"))

for i in range(amount):
    numbers.append(random.randint(0,100))


numbers.sort()

print(numbers)

numbers.pop()

print(numbers)
