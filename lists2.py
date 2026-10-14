numbers = [2,3,4,1,34,3,2,33,5,32,1,2,6,7,3,2,5]

#exercize
#ask a number
#print how many times number is in the list
myNumber = int(input("Write a number:").strip())

count = 0

for number in numbers:
    if myNumber == number:
        count += 1

print(myNumber,"is",count,"times in the list")


#ex: write a number: 2
#2 is 4 times in the list
