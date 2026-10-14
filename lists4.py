import random

print(random.randint(1,10))

abc = "abcdefghijklmnopqrstuvwxyz"
print(abc[random.randint(0,len(abc)-1)])

stringlen = random.randint(0,100)

newstring = ""

for i in range(stringlen):
    newstring += abc[random.randint(0,len(abc)-1)]

print(newstring)

for i in range(5):
    print(i)


