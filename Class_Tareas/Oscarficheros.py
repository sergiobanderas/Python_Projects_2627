import random

filename = input("Enter the filename: ")


try:
    f = open(filename)
    f.close()
    print(f"{filename} exists")
except FileNotFoundError:
    with open(filename, "w") as file:
        while True:
            minimum = int(input("Introduce the minimum number: "))
            maximum = int(input("Introduce the maximum number: "))
            lista = []
            for f in range(10):
                resultado = random.randint(minimum, maximum)
                lista.append(str(resultado))

            linea = ",".join(lista)
            file.write(linea + "\n")
            print(linea)

            ask = input("Do you want to add other line y/n: ")
            if ask == "n":
                break
            






