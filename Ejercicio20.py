#Clasificación de IMC

peso = float(input("Escribe tu peso en kg: "))
altura = float(input("Escribe tu altura en metros: "))

imc = peso / (altura ** 2)
print(f"Tu IMC es: {imc:.2f}")

if imc < 18.5:
    print("Clasificación: Bajo peso")
elif 18.5 <= imc <= 24.9:
    print("Clasificación: Normal")
elif 25 <= imc <= 29.9:
    print("Clasificación: Sobrepeso")
else:
    print("Clasificación: Obesidad")
