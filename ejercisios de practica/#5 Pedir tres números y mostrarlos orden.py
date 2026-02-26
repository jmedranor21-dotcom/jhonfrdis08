#5 Pedir tres números y mostrarlos ordenados de mayor a menor

# Pedir tres números
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

numeros = [num1, num2, num3]

numeros.sort(reverse=True)


print("Números ordenados de mayor a menor:", numeros)