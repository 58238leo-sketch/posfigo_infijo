from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.uic import loadUi

from estructuras.lineales.lista_enlazada_pila import LinkedStack


class MenuPila(QDialog):
    def __init__(self):
        super().__init__()

        loadUi("ui/pila.ui", self)

        self.pila = LinkedStack()

        self.btn_push.clicked.connect(self.push_pila)
        self.btn_pop.clicked.connect(self.pop_pila)
        
        self.btn_top.clicked.connect(self.ver_tope)
        self.btn_print.clicked.connect(self.mostrar_en_ventana)

    def push_pila(self):
        dato = self.txt_dato.text().strip()

        if dato == "":
            QMessageBox.warning(self, "Error", "Ingrese un dato válido para la pila")
            return

        self.pila.push(dato)
        self.txt_dato.clear()
        self.imprimir()

    def pop_pila(self):
        if not self.pila.pop():
            QMessageBox.warning(self, "Error", "La pila está vacía, no se puede hacer Pop")
            return

        self.imprimir()

    def ver_tope(self):
        elemento = self.pila.peek() 
        if elemento is None:
            QMessageBox.warning(self, "Top", "La pila está vacía.")
        else:
            QMessageBox.information(self, "Top de la Pila", f"El elemento en el tope es: {elemento}")

    def mostrar_en_ventana(self):
        estado_pila = self.pila.get_stack()
        
        mensaje = f"Contenido actual de la estructura:\n\n{estado_pila}"
        
        QMessageBox.information(self, "Impresión de Pila", mensaje)

    def imprimir(self):
        self.lbl_resultado.setText(self.pila.get_stack())