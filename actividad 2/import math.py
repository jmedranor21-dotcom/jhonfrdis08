import math
import random

# ==========================
# MODELOS
# ==========================

class Cliente:
    def __init__(self, id_cliente, nombre):
        self.id_cliente = id_cliente
        self.nombre = nombre


class Repartidor:
    def __init__(self, id_repartidor, nombre, ubicacion):
        self.id_repartidor = id_repartidor
        self.nombre = nombre
        self.ubicacion = ubicacion  # (x, y)
        self.disponible = True


class Pedido:
    def __init__(self, id_pedido, cliente, origen, destino, peso):
        self.id_pedido = id_pedido
        self.cliente = cliente
        self.origen = origen  # (x, y)
        self.destino = destino  # (x, y)
        self.peso = peso
        self.estado = "Registrado"
        self.tarifa = 0
        self.repartidor = None


# ==========================
# MOTOR DE RUTAS
# ==========================

class MotorRutas:

    @staticmethod
    def calcular_distancia(punto1, punto2):
        # Distancia euclidiana
        return math.sqrt((punto1[0] - punto2[0])**2 + 
                         (punto1[1] - punto2[1])**2)

    @staticmethod
    def calcular_ruta(origen, destino):
        distancia = MotorRutas.calcular_distancia(origen, destino)
        tiempo_estimado = distancia / 40 * 60  # Suponiendo 40 km/h
        return distancia, tiempo_estimado


# ==========================
# CALCULO DE TARIFAS
# ==========================

class CalculadoraTarifas:

    COSTO_KM = 2000
    FACTOR_PESO = 500

    @staticmethod
    def calcular_tarifa(distancia, peso):
        factor_demanda = random.randint(1000, 3000)
        tarifa = (distancia * CalculadoraTarifas.COSTO_KM) + \
                 (peso * CalculadoraTarifas.FACTOR_PESO) + \
                 factor_demanda
        return round(tarifa, 2)


# ==========================
# ASIGNACIÓN DE REPARTIDOR
# ==========================

class AsignadorRepartidores:

    @staticmethod
    def asignar_repartidor(pedido, lista_repartidores):
        disponibles = [r for r in lista_repartidores if r.disponible]

        if not disponibles:
            return None

        # Elegir el más cercano al punto de origen
        repartidor_cercano = min(
            disponibles,
            key=lambda r: MotorRutas.calcular_distancia(r.ubicacion, pedido.origen)
        )

        repartidor_cercano.disponible = False
        pedido.repartidor = repartidor_cercano
        pedido.estado = "Asignado"

        return repartidor_cercano


# ==========================
# SISTEMA PRINCIPAL
# ==========================

class SmartDeliverySystem:

    def __init__(self):
        self.pedidos = []
        self.repartidores = []

    def agregar_repartidor(self, repartidor):
        self.repartidores.append(repartidor)

    def registrar_pedido(self, pedido):
        print(f"\nRegistrando pedido {pedido.id_pedido}...")
        self.pedidos.append(pedido)

        # Calcular ruta
        distancia, tiempo = MotorRutas.calcular_ruta(pedido.origen, pedido.destino)

        # Calcular tarifa
        pedido.tarifa = CalculadoraTarifas.calcular_tarifa(distancia, pedido.peso)

        # Asignar repartidor
        repartidor = AsignadorRepartidores.asignar_repartidor(pedido, self.repartidores)

        if repartidor:
            print(f"Pedido asignado a {repartidor.nombre}")
        else:
            print("No hay repartidores disponibles")

        print(f"Distancia: {round(distancia,2)} km")
        print(f"Tiempo estimado: {round(tiempo,2)} minutos")
        print(f"Tarifa calculada: ${pedido.tarifa}")


# ==========================
# EJECUCIÓN DEL SISTEMA
# ==========================

if __name__ == "__main__":

    sistema = SmartDeliverySystem()

    # Crear repartidores
    sistema.agregar_repartidor(Repartidor(1, "Carlos", (2, 3)))
    sistema.agregar_repartidor(Repartidor(2, "Ana", (5, 1)))
    sistema.agregar_repartidor(Repartidor(3, "Luis", (8, 8)))

    # Crear cliente
    cliente1 = Cliente(1, "Juan Pérez")

    # Registrar pedido
    pedido1 = Pedido(101, cliente1, (1, 1), (7, 5), 3)

    sistema.registrar_pedido(pedido1)