# * Tarea - lista de ciudades
# * Idea: Crear una lista con nombre de ciudades y que no se repitan.
# ? Ingresar datos | Logica: usar 'Append' y Primero ver si la ciudad existe, si no existe agregar.
# ? Mostrar la lista
# ? Modificar el nombre de una ciudad
# ? Borrar una ciudad
# ? Salir
# TODO: Ciudades = [] //Lista vacia

print("1: Ingresar Ciudad")
print("2: Mostrar lista de Ciudades")
print("3: Modificar la ciudad")
print("4: Borrar la ciudad")
print("0: Salir")

ciudades=[]

while True:
    entrada=input("Ingrese una opcion: ")
    if(entrada == '1'):
        añadirCiudad=input("Ingrese una ciudad: ")
        busca=(añadirCiudad in ciudades)
        if busca == True:
            print("ERROR: La ciudad ya existe en la lista")
        else:      
            ciudades.append(añadirCiudad)
            print("La ciudad añadida correctamente!")
    elif(entrada == '2'):
        print("Lista de Ciudades")
        for ciudad in ciudades:
            print("-> ",ciudad)
    elif(entrada == '3'):
        largo=len(ciudades)
        for i in range(largo):
            print(i,"->", ciudades[i])
        numModifica=int(input("Ingrese el numero de la ciudad para modificar: "))
        nuevaCiudad=input("Ingrese la nueva ciudad: ")
        ciudades[numModifica]=nuevaCiudad
        print("La ciudad fue modificada correctamente!")
    elif(entrada == '4'):
        largo=len(ciudades)
        for i in range(largo):
            print(i,"->", ciudades[i])
        numModifica=int(input("Ingrese el numero de la ciudad para eliminar: "))
        del(ciudades[numModifica])
    elif(entrada == '0'):
        break
    else:
        print("Ingrese una opcion valida")