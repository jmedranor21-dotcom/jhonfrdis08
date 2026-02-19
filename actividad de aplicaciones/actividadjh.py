# ================== MODELO ==================
class Cliente:
    def __init__(self, **datos):
        self.datos = datos

class TechSolutions:
    SERVICIOS = {
        1: ("Desarrollo", 200),
        2: ("Soporte", 500),
        3: ("Consultoría", 200),
        4: ("Auditoría", 1500)
    }

    def registrar_cliente(self, **datos):
        return Cliente(**datos)

    def gestionar_servicios(self, *opciones):
        servicios, precios = [], []

        for op in opciones:
            if op in self.SERVICIOS:
                nombre, precio = self.SERVICIOS[op]
                servicios.append(nombre)
                precios.append(precio)

        subtotal = sum(precios)
        pares = len(servicios) // 2
        descuento = sum(sorted(precios)[:pares*2]) * 0.30
        total = subtotal - descuento

        return servicios, subtotal, descuento, total

# ================== FACTURACIÓN ==================
class Facturacion:
    @staticmethod
    def generar(cliente, *datos):
        servicios, subtotal, descuento, total = datos

        print("\n===== FACTURA TECH SOLUTIONS =====")
        for k, v in cliente.datos.items():
            print(f"{k.capitalize()}: {v}")

        print("\nServicios:", servicios)
        print("Subtotal: $", subtotal)
        print("Descuento: $", descuento)
        print("Total a pagar: $", total)

        return total

# ================== MOTOR DE NOTIFICACIONES ==================
def notificar(cliente, mensaje):
    print(f"\n📩 Mensaje enviado a {cliente.datos['nombre']} ({cliente.datos['email']}):")
    print("➡", mensaje)

# ================== SISTEMA INTERACTIVO ==================
sistema = TechSolutions()

# Registro cliente con validaciones
nombre = input("Nombre: ")

while True:
    id_cliente = input("ID (solo números): ")
    if id_cliente.isdigit():
        break
    print("💀 Error: El ID debe ser solo números.")

while True:
    email = input("Email: ")
    if "@" in email:
        break
    print("💀 Error: Email debe contener '@'.")

direccion = input("Dirección: ")

while True:
    telefono = input("Teléfono (solo números): ")
    if telefono.isdigit():
        break
    print("💀 Error: El teléfono debe contener solo números.")

cliente = sistema.registrar_cliente(
    nombre=nombre,
    id=id_cliente,
    email=email,
    direccion=direccion,
    telefono=telefono
)

# Mostrar servicios
print("\nServicios disponibles:")
for k, v in sistema.SERVICIOS.items():
    print(f"{k}. {v[0]} - ${v[1]}")
print("0. Terminar selección")

# Selección interactiva
opciones = []
while True:
    try:
        op = int(input("Ingresa el número del servicio (0 para terminar): "))
        if op == 0:
            break
        if op not in sistema.SERVICIOS:
            print("Opción inválida, intenta de nuevo.")
            continue
        opciones.append(op)
    except ValueError:
        print("Ingresa un número válido.")

pedido = sistema.gestionar_servicios(*opciones)
total = Facturacion.generar(cliente, *pedido)

# Callback con mensaje
mensaje = f"Su pedido fue procesado correctamente. Total pagado: ${total}"
notificar(cliente, mensaje)

