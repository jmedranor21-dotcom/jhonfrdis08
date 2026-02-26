#10
# Pedir el valor de la compra
compra = float(input("Ingrese el valor de la compra: "))

# Verificar si aplica descuento
if compra > 300000:
    descuento = compra * 0.20
    total = compra - descuento
else:
    total = compra

print("La cantidad a pagar es: $", round(total, 2))