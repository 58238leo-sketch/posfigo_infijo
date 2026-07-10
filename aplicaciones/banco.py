from datetime import datetime
from estructuras.lineales.lista_enlazada_cola import LinkedQueue

class ClienteBanco:
    """Clase contenedora para almacenar los datos individuales de cada cliente."""
    def __init__(self, numero_cliente):
        self.numero = numero_cliente
        self.hora_llegada = datetime.now()

class SimuladorBanco:
    def __init__(self):
        self.cola_clientes = LinkedQueue()
        self.total_atendidos = 0
        self.tiempo_total_segundos = 0.0

    def registrar_turno(self, numero_cliente):
        """Crea un cliente con su hora de llegada actual y lo encola."""
        nuevo_cliente = ClienteBanco(numero_cliente)
        self.cola_clientes.enqueue(nuevo_cliente)
        return nuevo_cliente.hora_llegada.strftime("%H:%M:%S")

    def atender_cliente(self):
        """Desencola al primer cliente en espera y calcula los tiempos de permanencia."""
        if self.cola_clientes.is_empty():
            return None # No hay clientes en cola

        # Obtenemos el objeto ClienteBanco del frente de la cola
        cliente = self.cola_clientes.firstQueue()
        self.cola_clientes.dequeue()
        
        hora_salida = datetime.now()
        # Calculamos la diferencia de tiempo
        duracion = hora_salida - cliente.hora_llegada
        duracion_segundos = duracion.total_seconds()
        
        # Acumulamos estadísticas del banco
        self.total_atendidos += 1
        self.tiempo_total_segundos += duracion_segundos
        
        return {
            "numero": cliente.numero,
            "llegada": cliente.hora_llegada.strftime("%H:%M:%S"),
            "salida": hora_salida.strftime("%H:%M:%S"),
            "duracion": f"{duracion_segundos:.2f} seg"
        }

    def obtener_cola_texto(self):
        """Genera una representación de texto con los turnos vigentes."""
        if self.cola_clientes.is_empty():
            return "No hay clientes en espera."
        
        elementos = []
        # Recorremos la cola a través de sus nodos para no vaciarla al imprimir
        actual = self.cola_clientes.front
        while actual:
            cliente = actual.data
            elementos.append(f"Turno: {cliente.numero} (Llegó: {cliente.hora_llegada.strftime('%H:%M:%S')})")
            actual = actual.next
        return "\n".join(elementos)

    def cerrar_banco(self):
        """Verifica si quedan pendientes o calcula promedios generales."""
        if not self.cola_clientes.is_empty():
            return {"estado": "pendiente", "mensaje": "Hay clientes por atender"}
        
        promedio = 0.0
        if self.total_atendidos > 0:
            promedio = self.tiempo_total_segundos / self.total_atendidos
            
        return {
            "estado": "exito",
            "atendidos": self.total_atendidos,
            "promedio": f"{promedio:.2f} seg"
        }