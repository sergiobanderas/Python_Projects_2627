import os, random, sys
respuesta="test"
nombre_fichero=input("Introduce el nombre del fichero --> ")

if os.path.exists(nombre_fichero):
        print(f"Error: El fichero '{nombre_fichero}' ya existe. No se puede volver a crear.")
else:
	print(f"El fichero no existe y ha sido creado")



while True:
        minimo=int(input("mínimo: "))
        maximo=int(input("máximo: "))

        if minimo > maximo:
                print("Error: El mínimo no puede ser mayor que el máximo. Inténtalo de nuevo.")
                sys.exit()

        
        with open(nombre_fichero,"a") as file:
                for n in range(10):
                        numero=int(random.randint(minimo,maximo))
                        coma = "," if n < 9 else ""                      
                        file.write(f"{numero}{coma}")
                file.write("\n")

        respuesta="test"
        salir = False
        while respuesta.upper() not in ["Y", "N"]:
                respuesta = input("¿Deseas añadir otra línea? Y / N --> ").strip()
                if respuesta.upper() == "N":
                        salir = True

        if salir:
                break

print ("FIN")