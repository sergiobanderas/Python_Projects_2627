import os
import random

# 1. Preguntar el nombre del fichero
#  (y comprobar si ya existe)
while True:
    nombre = input("Introduce el nombre del fichero: ").strip()
    if os.path.exists(nombre):
        print("El fichero ya existe, elige otro nombre")
    else:
        break

# 2. Crear el fichero y escribir las líneas
with open(nombre, "w") as f:

    while True:
        # 3. Preguntar número minimo
        minimo = int(input("Mínimo: "))

        # 4. Preguntar número máximo
        maximo = int(input("Máximo: "))

        # 5. Crear una fila con 10 números 
        # aleatorios separados por comas
        linea = ""
        for i in range(10):
            linea += str(random.randint(minimo, maximo)) + ","

        linea = linea[:-1]
        f.write(linea + "\n")

        # 6. Preguntar si quiere añadir otra línea (y/n)
        while True:
            pregunta = input("¿Quieres añadir otra línea? y/n: ").lower().strip()
            if pregunta == "y" or pregunta == "n":
                break
            else:
                print("Escribe solo y o n")

        if pregunta == "n":
            break

# 7. Terminar
print("Fin")