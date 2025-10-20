#Cálculo de impuestos

salario = float(input("Digita tu salario mensual por favor: "))

if salario < 10000:
    impuesto = 0
elif salario <= 30000:
    impuesto = salario * 0.10
else:
    impuesto = salario * 0.20

print(f"Tu impuesto a pagar es: ${impuesto:.2f}")
