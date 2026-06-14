from estructuras.lineales.nodo import Node
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert_at_beginning(self, data):
        #paso1: crear un nuevo nodo con el dato proporcionado
        new_node = Node(data)
        #paso2: verificar si la lista esta vacia
        if self.head is None and self.tail is None:
            #si la lista esta vacia, el nuevo nodo se convierte en la cabeza y la cola
            self.head = new_node
            self.tail = new_node
        else:
            #si la lista no esta vacia, el nuevo nodo apunta a la cabeza actual
            new_node.next = self.head
            #el nuevo nodo se convierte en la nueva cabeza de la lista
            self.head = new_node
            
    def print_linked_list(self):
            temp = self.head
            print("Head -> ", end="")
            while temp is not None:
                print(temp.data,"->", end=" ")
                temp = temp.next
            print("<- Tail")