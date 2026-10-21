from function1 import *
import random

texto=""
for n in range(10):
    hola()
    texto += adios(str(n))

print(texto)

age = writeNumber("Age:")

if ageControl(age):
    print("You can access")
else:
    print("No access")


min, max = inputMinMax()
print("Min:",min,"Max:",max)

randomNumber = random.randint(min,max)
print("Random number between",min,"and",max,":",randomNumber)

