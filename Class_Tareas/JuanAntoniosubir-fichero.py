import random

#Ask name file
name = input("Introduce el nombre del fichero(con extensión): ")

#Create file
try:     
    file = open(name, "x")
    print("El fichero se ha creado correctamente")

except FileExistsError:
    print("El fichero ya existe")
    exit()

#Preguntar número mínimo
minNumber = int(input("Introduce el número mínimo aleatorio: "))

#Preguntar número máximo
maxNumber = int(input("Introduce el número máximo aleatorio: "))


filename = name

#Crear 1 fila con 10 números aleatorios
with open(filename, "a") as file:
    listnumber = []
    for n in range(10):
        listnumber.append (random.randint(minNumber, maxNumber))
        print(listnumber)
    for n in listnumber:
            file.write(str(n) + ",")
    file.write("\n")

#Preguntar si quiere añadir otra línea
    while True:
        askQuestion = input("¿Quieres añadir alguna línea más? y/n: ").lower()
        if askQuestion == "y":
            minNumber = int(input("Introduce el número mínimo aleatorio: "))
            maxNumber = int(input("Introduce el número máximo aleatorio: "))
            listnumber2 = []
            for n in range(10):
                    listnumber2.append (random.randint(minNumber, maxNumber))
                    print(listnumber2)
            for n in listnumber2:
                    file.write(str(n) + ",")
            file.write("\n")
        elif askQuestion !="y" and askQuestion !="n":
            print("Solo es válido y o n")
        if askQuestion == "n":
#Terminar
            break

