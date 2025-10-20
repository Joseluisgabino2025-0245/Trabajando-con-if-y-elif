#Calculadora de tres descuentos

precio = float(input("Diga el precio del producto:"))

if precio < 50:
    descuento = 0
elif 50 <= precio <= 100:
    descuento = precio * 0.05
else:
    descuento = precio * 0.10

precio_final = precio - descuento
print(f"Descuento aplicado: ${descuento:.2f}")
print(f"Precio final: ${precio_final:.2f}")
