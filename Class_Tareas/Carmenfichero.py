import random

def nuevaFila():
    numbers = []
    # puntos 3 y 4
    min = int(input("Escribe el número mínimo: "))
    max = int(input("Escribe el número máximo: "))

    # punto 5
    for i in range(10):
        numbers.append(random.randint(min,max))
    file.write(str(numbers) + "\n")

# punto 1
filename = input("Escribe el nombre de un fichero: ")

# punto 2
with open(filename,"w") as file:

    nuevaFila()

    while True:
        # punto 6
        ans = input("¿Quieres escribir una nueva línea? y / n: ").lower().strip()
        if ans == "y":
            nuevaFila()
        elif ans == "n":
            # punto 7
            print("Fin")
            break
        else:
            print("escribe solo y o n")