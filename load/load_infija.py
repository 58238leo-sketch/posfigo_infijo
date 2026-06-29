from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.uic import loadUi

from aplicaciones.lista_infija import ConvertidorInfijoPosfijo


class MenuInfija(QDialog):
    def __init__(self):
        super().__init__()

        
        loadUi("ui/infija.ui", self)

        # Instanciamos la clase convertidora
        self.convertidor = ConvertidorInfijoPosfijo()

       
        self.btn_calcular.clicked.connect(self.procesar_conversion)

    def procesar_conversion(self):
        
        expresion = self.txt_infija.text().strip()

        
        if expresion == "":
            QMessageBox.warning(self, "Error", "Por favor, ingrese una expresión infija.")
            return

        # Realizamos la conversión llamando al método del objeto convertidor
        resultado = self.convertidor.convertir(expresion)

        
        self.lbl_resultado.setText(resultado)