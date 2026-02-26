#11
# Pedir un número de tres cifras
numero = input("Ingrese un número de tres cifras: ")

# Verificar que tenga exactamente 3 dígitos
if len(numero) == 3 and numero.isdigit():
    if numero[0] == numero[2]:
        print("El número es capicúa.")
    else:
        print("El número no es capicúa.")
else:
    print("Número inválido. Debe tener 3 cifras.")