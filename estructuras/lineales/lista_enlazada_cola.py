from estructuras.lineales.nodo import Node

class LinkedQueue:
    def __init__(self):
        
        self.front = None
        self.back = None

    def is_empty(self):
        """Método auxiliar solicitado para comprobar si la cola está vacía."""
        return self.front is None

    def enqueue(self, dato):
        """Inserta un elemento al final de la cola (Back)."""
        nuevo_nodo = Node(dato)
        
        # Si la cola está vacía, el nuevo nodo es tanto el frente como el final
        if self.is_empty():
            self.front = nuevo_nodo
            self.back = nuevo_nodo
        else:
            # El nodo que estaba al final ahora apunta al nuevo nodo
            self.back.next = nuevo_nodo
            # Actualizamos nuestro puntero del final hacia el nuevo nodo
            self.back = nuevo_nodo

    def dequeue(self):
        """Elimina el elemento al frente de la cola (Front). Retorna False si está vacía."""
        if self.is_empty():
            return False
        
        # Avanzamos el frente al siguiente nodo de la fila
        self.front = self.front.next
        
        # Si al avanzar el frente quedó vacío, significa que la cola se quedó sin elementos
        if self.front is None:
            self.back = None
            
        return True

    def firstQueue(self):
        """Retorna el dato del primer elemento en la cola sin eliminarlo."""
        if self.is_empty():
            return None
        return self.front.data

    def lastQueue(self):
        """Retorna el dato del último elemento en la cola sin eliminarlo."""
        if self.is_empty():
            return None
        return self.back.data

    def printQueue(self):
        """Recorre la cola y devuelve una cadena de texto representativa."""
        if self.is_empty():
            return "Cola vacía"
        
        elementos = []
        actual = self.front
        while actual:
            elementos.append(str(actual.data))
            actual = actual.next
            
        # Representación visual simulando una fila india (Frente <- ... <- Final)
        return " <- ".join(elementos)