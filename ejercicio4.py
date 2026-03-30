cantidad = int(input("Cuantos numeros vamos a poner: "))

lista_num = []
while len(lista_num) != cantidad:
    num = int(input("Ingresa un num entero: "))
    lista_num.append(num)
print(f"Lista desordenada: {lista_num}")

for i in range(len(lista_num)):
    for j in range(len(lista_num) - 1):
        if lista_num[j] > lista_num[j+1]:
            lista_num[j], lista_num[j+1] = lista_num[j+1], lista_num[j]

print(f"Lista ordenada: {lista_num}")

# Complejidad Big O = O(n²)
# Justificación = Utiliza dos bucles anidados para comparar y ordenar los elementos de la lista. Esto significa que el tiempo de ejecución aumenta proporcionalmente al cuadrado del número de elementos, característica del algoritmo Bubble Sort.
