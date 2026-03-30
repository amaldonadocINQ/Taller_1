listanum = []
cantidad = int(input("Ingrese la cantidad de números que desea ingresar: "))
for i in range(cantidad):
    numero = int(input(f"Ingrese el número {i + 1}: "))
    listanum.append(numero)
busqueda = input("Ingrese el número que desea buscar: ")
for i in range(cantidad):
    if busqueda == str(listanum[i]):
        print(f"El número {busqueda} se encuentra en la posición {i + 1}.")
    else:
        print(f"El número {busqueda} no se encuentra en la lista.")
    break

# Complejidad Big O: O(n) 
# Justificación: Se recorre la lista una vez para buscar el número.
