#8
dia = int(input("Día: "))
mes = int(input("Mes: "))
anio = int(input("Año: "))

# Avanzar al día siguiente
dia += 1

if dia > 30:
    dia = 1
    mes += 1

if mes > 12:
    mes = 1
    anio += 1

print("La fecha del día siguiente es:", dia, "/", mes, "/", anio)