from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic

from load.load_lista_enlazada_simple import MenuListaEnlazada
from load.load_lista_pila import MenuPila
from load.load_infija import MenuInfija



class MenuPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi("ui/menu_principal.ui", self)

        self.actionLista_Enlazada.triggered.connect(
            self.abrir_lista_enlazada
        )
        self.actionPilas.triggered.connect(self.abrir_pilas)

        self.actionInfija.triggered.connect(self.abrir_infija)

        self.action5_Salir.triggered.connect(self.close)




    def abrir_lista_enlazada(self):
        self.ventana_lista = MenuListaEnlazada()
        self.ventana_lista.show()

    def abrir_pilas(self):
        self.ventana_pila = MenuPila()
        self.ventana_pila.show()


    def abrir_infija(self):
        self.ventana_infija = MenuInfija()
        self.ventana_infija.show()

    