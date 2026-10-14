import random
import os

fileName = input("Nombre del fichero:")

# Check if the specified file exists and creates it if it doesn't.
if os.path.isfile(fileName):
    print("ERROR: El fichero ya existe. Prueba con otro nombre.")
    exit()
else:
    open(fileName, "x").close()

continueWriting = "y"

# Start single line loop. Will repeat until the user declines.
while continueWriting == "y":
    numMin = int(input("Introduce el número mínimo: "))
    numMax = int(input("Introduce el número máximo: "))
    index = 0
    lineLen = 10
    numberList = []

# Loop for selecting 10 random numbers within the specified range.
    while index < lineLen:
        numberList.append(random.randint(numMin, numMax))
        index += 1

# Build the final line and write on the file.
    numberLine = ",".join(str(n) for n in numberList)
    with open(fileName, "a") as f:
        f.write(numberLine + "\n")

    continueWriting = input("¿Quieres añadir otra línea? (y/n)").strip().lower()