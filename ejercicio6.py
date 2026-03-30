while True:
    try:
        num = int(input("Cuántos números vas a ingresar?: "))
        break
    except:
        print("Debes dar un número entero positivo.")

Lista=[]
for x in range(num):
    while True:
        try:
            j = float(input(f"Ingrese número {x+1}: "))
            break
        except:
            print("Debes dar un número entero positivo.")
    Lista.append(j)

print("Parejas:")
for x in range(len(Lista)):
    for j in range((len(Lista))):
        if x != j:
            print(f"({Lista[x]:.0f}, {Lista[j]:.0f})")

# Complejidad Big O: O(n²)
# Justificación = Si el tamaño de la lista es n, entonces: El primer bucle se ejecutará n veces. Por cada iteración del primer bucle, el segundo también se ejecuta n veces.