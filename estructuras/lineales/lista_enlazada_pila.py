from estructuras.lineales.nodo import Node

class LinkedStack:
    def __init__(self):
        self.top = None  

    def push(self, dato):
        """Inserta un elemento en el tope de la pila."""
        nuevo_nodo = Node(dato) 
        if self.is_empty():
            self.top = nuevo_nodo
        else:
            nuevo_nodo.next = self.top 
            self.top = nuevo_nodo

    def pop(self):
        """Elimina el elemento en el tope de la pila. Retorna False si está vacía."""
        if self.is_empty():
            return False
        
        self.top = self.top.next
        return True

    def peek(self):
        """Retorna el valor del elemento en el tope SIN eliminarlo. 
        Si la pila está vacía, retorna None."""
        if self.is_empty():
            return None
        return self.top.data  

    def is_empty(self):
        """Verifica si la pila está vacía."""
        return self.top is None

    def get_stack(self):
        """Recorre la pila y devuelve una cadena de texto para la interfaz."""
        if self.is_empty():
            return "Pila vacía"
        
        elementos = []
        actual = self.top
        while actual:
            elementos.append(str(actual.data)) 
            actual = actual.next 
        
        return " -> ".join(elementos)