#Tipo de triangulos

lado1 = float(input("Diga la primera longitud: "))
lado2 = float(input("Diga la segunda longitud: "))
lado3 = float(input("Diga la tercera longitud: "))

if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
    if lado1 == lado2 == lado3:
        print("El triángulo es equilátero.")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("El triángulo es isósceles.")
    else:
        print("El triángulo es escaleno.")
else:
    print("Las longitudes no pueden formar un triángulo.")
