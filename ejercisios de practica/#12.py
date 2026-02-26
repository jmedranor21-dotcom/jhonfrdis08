#12
# Pedir la cantidad de llantas
cantidad = int(input("Ingrese la cantidad de llantas a comprar: "))

# Determinar el precio por unidad
if cantidad < 5:
    precio_unitario = 30000
elif 5 <= cantidad <= 10:
    precio_unitario = 25000
else:
    precio_unitario = 20000

# Calcular el total
total = cantidad * precio_unitario

# Mostrar resultados
print(f"Precio por llanta: ${precio_unitario}")
print(f"Total a pagar: ${total}")