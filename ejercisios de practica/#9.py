#9
nota = int(input("Ingrese una nota (0-10): "))

numeros = ["cero", "uno", "dos", "tres", "cuatro",
           "cinco", "seis", "siete", "ocho", "nueve", "diez"]

if 0 <= nota <= 10:
    print("La nota es:", numeros[nota])
else:
    print("Nota inválida.")