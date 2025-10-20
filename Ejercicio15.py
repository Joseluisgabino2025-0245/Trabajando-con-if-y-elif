#Comparación de tres longitudes

lado1 = float(input("Digite la primera longitud: "))
lado2 = float(input("Digite la segunda longitud: "))
lado3 = float(input("digite la tercera longitud: "))

if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
    print("Sí pueden formar un triángulo.")
else:
    print("No pueden formar un triángulo.")
