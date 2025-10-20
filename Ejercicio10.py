#Clasificación de ángulos

angulo = float(input("Ingresa el valor del ángulo en grados por favor: "))

if angulo < 90:
    print("El ángulo es agudo.")
elif angulo == 90:
    print("El ángulo es recto.")
elif angulo > 90 and angulo < 180:
    print("El ángulo es obtuso.")
elif angulo == 180:
    print("El ángulo es llano.")
else:
    print("El ángulo no pertenece a los tipos básicos.")
