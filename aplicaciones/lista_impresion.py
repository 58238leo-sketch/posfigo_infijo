from estructuras.lineales.lista_enlazada_cola import LinkedQueue

class TrabajoImpresion:
    """Encapsula las propiedades de un documento a imprimir."""
    def __init__(self, consecutivo, usuario, documento, paginas):
        self.consecutivo = consecutivo
        self.usuario = usuario
        self.documento = documento
        self.paginas = int(paginas)

    def __str__(self):
        return f"ID: {self.consecutivo} | Doc: {self.documento} | Usuario: {self.usuario} ({self.paginas} págs)"

class GestorImpresion:
    """Administra el flujo de los trabajos de impresión utilizando LinkedQueue."""
    def __init__(self):
        self.cola_trabajos = LinkedQueue()
        self.consecutivo_actual = 1

    def agregar_trabajo(self, usuario, documento, paginas):
        """Operación: ENQUEUE (Encolar)"""
        if not usuario.strip() or not documento.strip():
            raise ValueError("El usuario y el nombre del documento no pueden estar vacíos.")
        
        try:
            pags = int(paginas)
        except ValueError:
            raise ValueError("El número de páginas debe ser un número entero.")

        if pags < 1:
            raise ValueError("El número de páginas debe ser mayor o igual a 1.")

        # Creamos la instancia de TrabajoImpresion
        nuevo_trabajo = TrabajoImpresion(self.consecutivo_actual, usuario.strip(), documento.strip(), pags)
        self.cola_trabajos.enqueue(nuevo_trabajo)
        self.consecutivo_actual += 1
        return nuevo_trabajo

    def imprimir_siguiente(self):
        """Operación: DEQUEUE (Desencolar)"""
        if self.cola_trabajos.is_empty():
            raise IndexError("La cola de impresión está vacía. No hay trabajos para procesar.")
        
        trabajo = self.cola_trabajos.firstQueue()
        self.cola_trabajos.dequeue()
        return trabajo

    def ver_frente(self):
        """Operación: FRONT/PEEK (Consultar el primero)"""
        if self.cola_trabajos.is_empty():
            return None
        return self.cola_trabajos.firstQueue()

    def obtener_total_pendientes(self):
        """Operación: SIZE (Contar elementos sin vaciar la cola)"""
        total = 0
        actual = self.cola_trabajos.front
        while actual is not None:
            total += 1
            actual = actual.next
        return total

    def obtener_lista_pendientes(self):
        """Recorre la cola desde el frente hasta el final en orden FIFO"""
        lista = []
        actual = self.cola_trabajos.front
        while actual is not None:
            lista.append(actual.data)
            actual = actual.next
        return lista