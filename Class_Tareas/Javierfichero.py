import random

nombre = input("Nombre del fichero: ")

fichero = open(nombre, "w")

seguir = "y"
while seguir == "y":
    minimo = int(input("mínimo: "))
    maximo = int(input("máximo: "))

    linea = ""
    for i in range(10):
        num = random.randint(minimo, maximo)
        if i == 0:
            linea = str(num)
        else:
            linea = linea + "," + str(num)

    fichero.write(linea + "\n")
    print("---> " + linea)

    seguir = input("quiere añadir otra línea y/n: ")

fichero.close()
print("fin")