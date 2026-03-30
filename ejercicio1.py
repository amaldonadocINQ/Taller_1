lista = []

num1 = int(input("Ingresa el num 1: "))
num2 = int(input("Ingresa el num 2: "))
num3 = int(input("Ingresar el num 3: "))

lista.append(num1)
lista.append(num2)
lista.append(num3)

promedio = sum(lista)/len(lista)
print(promedio)

# Complejidad Big O: O(1) 
# Justificación: El número de operaciones es siempre el mismo. El programa solo pide tres números, los agrega a la lista y calcula el promedio, sin importar el tamaño de la entrada, por lo que el tiempo de ejecución no cambia.
