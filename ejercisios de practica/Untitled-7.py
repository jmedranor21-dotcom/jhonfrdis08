
#7

dia = int(input("Día: "))
mes = int(input("Mes: "))
anio = int(input("Año: "))

if anio > 0 and 1 <= mes <= 12 and 1 <= dia <= (
    31 if mes in [1,3,5,7,8,10,12] 
    else 30 if mes in [4,6,9,11] 
    else 28):
    print("La fecha es correcta.")
else:
    print("La fecha es incorrecta.")