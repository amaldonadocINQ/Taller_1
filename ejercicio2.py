cantidad = int(input("Cuantos numeros vamos a poner: "))

lista_num = []
while len(lista_num) != cantidad:
    num = int(input("Ingresa un num entero: "))
    lista_num.append(num)
    
maximo = max(lista_num)
minimo = min(lista_num)
print(f"El maximo es {maximo}, y el minimo es {minimo}, la lista es: \n {lista_num}")

# Complejidad Big O: O(n)
# Justificación = El programa recorre la lista de números una cantidad proporcional al tamaño de la entrada (cantidad). Las funciones max() y min() también recorren la lista una vez cada una, por lo que el tiempo de ejecución crece linealmente con el número de elementos.