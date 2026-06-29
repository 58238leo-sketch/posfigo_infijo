from estructuras.lineales.lista_enlazada_pila import LinkedStack

class ConvertidorInfijoPosfijo:
    def __init__(self):
        # Definimos la precedencia de los operadores básicos solicitados
        self.precedencia = {
            '+': 1, '-': 1,
            '*': 2, '/': 2,
            '$': 3  
        }

    def es_operador(self, caracter):
        return caracter in self.precedencia

    def obtener_precedencia(self, operador):
        return self.precedencia.get(operador, 0)

    def convertir(self, expresion_infija):
        """Convierte una expresión infija válida a posfija usando LinkedStack."""
        pila_operadores = LinkedStack()
        resultado_posfijo = []
        
        # Eliminamos espacios en blanco redundantes de la expresión
        expresion_limpia = expresion_infija.replace(" ", "")

        for caracter in expresion_limpia:
            # 1. Si es operando (letra o número), va directo al resultado
            if caracter.isalnum():
                resultado_posfijo.append(caracter)
                
            # 2. Si es paréntesis de apertura, va a la pila
            elif caracter == '(':
                pila_operadores.push(caracter)
                
            # 3. Si es paréntesis de cierre, vaciamos hasta encontrar el '('
            elif caracter == ')':
                while not pila_operadores.is_empty() and pila_operadores.peek() != '(':
                    # Obtenemos el operador del tope, lo sumamos al resultado y hacemos pop
                    operador_tope = pila_operadores.peek()
                    resultado_posfijo.append(operador_tope)
                    pila_operadores.pop()
                
                # Eliminamos el '(' sobrante de la pila
                if not pila_operadores.is_empty():
                    pila_operadores.pop()
                    
            # 4. Si es un operador básico
            elif self.es_operador(caracter):
                while (not pila_operadores.is_empty() and 
                       pila_operadores.peek() != '(' and 
                       self.obtener_precedencia(pila_operadores.peek()) >= self.obtener_precedencia(caracter)):
                    
                    resultado_posfijo.append(pila_operadores.peek())
                    pila_operadores.pop()
                
                pila_operadores.push(caracter)

        # 5. Vaciar los operadores restantes de la pila al finalizar el recorrido
        while not pila_operadores.is_empty():
            resultado_posfijo.append(pila_operadores.peek())
            pila_operadores.pop()

        # Retornamos los caracteres unidos con espacios para que sea legible
        return " ".join(resultado_posfijo)