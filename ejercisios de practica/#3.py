#3
# Pedir dos números al usuario
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))

# Verificar que ninguno sea cero para evitar error
if numero1 == 0 or numero2 == 0:
    print("No se puede determinar múltiplos con el número cero.")
else:
    # Verificar si uno es múltiplo del otro
    if numero1 % numero2 == 0:
        print(f"{numero1} es múltiplo de {numero2}.")
    elif numero2 % numero1 == 0:
        print(f"{numero2} es múltiplo de {numero1}.")
    else:
        print("Ninguno es múltiplo del otro.")