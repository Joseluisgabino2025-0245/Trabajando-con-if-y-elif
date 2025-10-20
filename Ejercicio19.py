#Conversión de horas a turnos

hora = int(input("Ingresa la hora (0-23) por favor: "))

if 6 <= hora <= 11:
    print("Mañana")
elif 12 <= hora <= 17:
    print("Tarde")
elif 18 <= hora <= 23:
    print("Noche")
elif 0 <= hora <= 5:
    print("Madrugada")
else:
    print("Hora inválida. Debe estar entre 0 y 23.")
