myList = [3,4,5,6,6,7,3,3,2,2,4,4,5]

#list length
print(len(myList))
print(myList)

myNumber = int(input("write a number:").strip())

index = 0

for number in myList:
    myList[index] *= myNumber
    index +=1

print(myList)
