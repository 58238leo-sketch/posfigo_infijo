from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic

from load.load_lista_enlazada_simple import MenuListaEnlazada
from load.load_lista_pila import MenuPila
from load.load_infija import MenuInfija
from load.load_lista_cola import MenuCola
from load.load_banco import MenuBanco



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

        self.actionCola.triggered.connect(self.abrir_cola)

        self.actionBanco.triggered.connect(self.abrir_banco)




    def abrir_lista_enlazada(self):
        self.ventana_lista = MenuListaEnlazada()
        self.ventana_lista.show()

    def abrir_pilas(self):
        self.ventana_pila = MenuPila()
        self.ventana_pila.show()


    def abrir_infija(self):
        self.ventana_infija = MenuInfija()
        self.ventana_infija.show()

    def abrir_cola(self):
        self.ventana_cola = MenuCola()
        self.ventana_cola.show()

    def abrir_banco(self):
        self.ventana_banco = MenuBanco()
        self.ventana_banco.show()

    