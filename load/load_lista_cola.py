from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.uic import loadUi
from estructuras.lineales.lista_enlazada_cola import LinkedQueue

class MenuCola(QDialog):
    def __init__(self):
        super().__init__()
        loadUi("ui/cola.ui", self)
        
        self.cola = LinkedQueue()

        
        self.btn_enqueue.clicked.connect(self.ejecutar_enqueue)
        self.btn_dequeue.clicked.connect(self.ejecutar_dequeue)
        self.btn_first.clicked.connect(self.ver_primero)
        self.btn_last.clicked.connect(self.ver_ultimo)
        self.btn_print.clicked.connect(self.mostrar_en_ventana)

    def ejecutar_enqueue(self):
        dato = self.txt_dato.text().strip()
        if dato == "":
            QMessageBox.warning(self, "Error", "Ingrese un dato válido")
            return
        self.cola.enqueue(dato)
        self.txt_dato.clear()
        self.actualizar_interfaz()

    def ejecutar_dequeue(self):
        if not self.cola.dequeue():
            QMessageBox.warning(self, "Error", "La cola está vacía")
            return
        self.actualizar_interfaz()

    def ver_primero(self):
        primero = self.cola.firstQueue()
        if primero is None:
            QMessageBox.warning(self, "First", "La cola está vacía")
        else:
            QMessageBox.information(self, "Primer Elemento", f"El frente de la cola es: {primero}")

    def ver_ultimo(self):
        ultimo = self.cola.lastQueue()
        if ultimo is None:
            QMessageBox.warning(self, "Last", "La cola está vacía")
        else:
            QMessageBox.information(self, "Último Elemento", f"El final de la cola es: {ultimo}")

    def mostrar_en_ventana(self):
        QMessageBox.information(self, "Print Queue", f"Estado de la cola:\n\n{self.cola.printQueue()}")

    def actualizar_interfaz(self):
        self.lbl_resultado.setText(self.cola.printQueue())