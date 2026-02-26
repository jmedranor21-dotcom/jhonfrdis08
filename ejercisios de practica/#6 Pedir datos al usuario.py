#6 Pedir datos al usuario
dia = int(input("Ingrese el día: "))
mes = int(input("Ingrese el mes: "))
anio = int(input("Ingrese el año: "))

# Validar fecha (todos los meses tienen 30 días)
if anio > 0:
    if mes >= 1 and mes <= 12:
        if dia >= 1 and dia <= 30:
            print("La fecha es correcta.")
        else:
            print("La fecha es incorrecta: día inválido.")
    else:
        print("La fecha es incorrecta: mes inválido.")
else:
    print("La fecha es incorrecta: año inválido.")