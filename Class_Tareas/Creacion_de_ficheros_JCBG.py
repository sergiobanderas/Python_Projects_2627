import random

print("***************************************")
print("******  Creación de ficheros :)  ******")
print("***************************************")


#Pedimos nombre de fichero
nombreFichero = input("Dame un nombre para tu fichero:").strip()

#Comprobamos que no exista
try:
    fichero = open(nombreFichero, "x")
    print("Tu fichero se ha creado.")

except FileExistsError:
    print("El fichero ya existe")
    exit()

#Pedimos numero minimo para el aleatorio
minimoAleatorio = int(input("Dame un número mínimo para el aleatorio:").strip())
#Pedimos numero maximo para el aleatorio
maximoAleatorio = int(input("Dame un número maximo para el aleatorio:").strip())

#Abrimos el fichero para escribir en el
fichero = open(nombreFichero, "w")

#Creamos la lista y la metemos
for n in range(10):
    numero = random.randint(minimoAleatorio ,maximoAleatorio)
    fichero.write(str(numero))

    if n < 9:
        fichero.write(",")
#cerramos el fichero 
fichero.close()

print("!!Linea añadida¡¡")


#Creamos un bucle para preguntar si queremos añadir linea
while True:
    #preguntamos si queremos añadir linea
    añadirLinea = input("¿Quieres añadir otra linea? S/N:").strip().upper()

    if añadirLinea == "S":
        minimoAleatorio = int(input("Dame un número mínimo para el aleatorio:").strip())

        maximoAleatorio = int(input("Dame un número maximo para el aleatorio:").strip())

        fichero = open(nombreFichero, "a")
        fichero.write("\n")
        for n in range(10):
            numero = random.randint(minimoAleatorio ,maximoAleatorio)
            fichero.write(str(numero))

            if n < 9:
                fichero.write(",")

        fichero.close()

    elif añadirLinea == "N":
            print("No quieres añadir otra linea, Gracias.")
            break
    
    else:
        print("Introduce un caracter valido porfa:")