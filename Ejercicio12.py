#Clasificación de números

numer1 = float(input("Ingresa el primer número: "))
numer2 = float(input("Ingresa el segundo número: "))
numer3 = float(input("Ingresa el tercer número: "))

if numer1 > 0 and numer2 > 0 and numer3 > 0:
    print("Todos los números son positivos.")
elif numer1 < 0 and numer2 < 0 and numer3 < 0:
    print("Todos los números son negativos.")
elif numer1 == 0 or numer2 == 0 or numer3 == 0:
    print("Hay al menos un número que es cero.")
else:
    print("Los números son mixtos (positivos y negativos).")
