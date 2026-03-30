while True:
    try:
        num = int(input(f"\nIngrese un número: "))
        break
    except:
        print(f"\nDebes dar un número entero positivo.")
    
contador = 0
print(" ")
while True:
    print (f"{num:.0f}/2 = {(num/2):.0f}")
    num = num//2
    contador = contador +1
    if num <= 1:
        break

print(f"\nEl número se dividió {contador:.0f} veces")

# Complejidad Big O: O(log n)
# Justificación: Existe una división para dos en el número, por ello el valor de num se reduce a la mitad en cada paso. Con esto, el número de iteraciones necesarias para que num llegue a 1 es proporcional a cuántas veces se puede dividir entre 2