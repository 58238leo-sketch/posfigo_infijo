from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.uic import loadUi
from aplicaciones.banco import SimuladorBanco

class MenuBanco(QDialog):
    def __init__(self):
        super().__init__()
        # Cargamos la interfaz de la ventanilla del banco
        loadUi("ui/banco.ui", self)
        
        self.simulador = SimuladorBanco()
        
        # Conexiones de los botones (nombres del Object Inspector)
        self.btn_turno.clicked.connect(self.solicitar_turno)
        self.btn_atender.clicked.connect(self.atender_siguiente)
        self.btn_cerrar.clicked.connect(self.procesar_cierre)

    def solicitar_turno(self):
        num_cliente = self.txt_cliente.text().strip()
        if num_cliente == "":
            QMessageBox.warning(self, "Error", "Ingrese un número de cliente")
            return
            
        hora_reg = self.simulador.registrar_turno(num_cliente)
        
        # Limpiamos input y actualizamos campos
        self.txt_cliente.clear()
        self.lbl_resultado_turno.setText(self.simulador.obtener_cola_texto())
        QMessageBox.information(self, "Turno Creado", f"Cliente {num_cliente} registrado a las {hora_reg}")

    def atender_siguiente(self):
        datos_atencion = self.simulador.atender_cliente()
        
        if datos_atencion is None:
            QMessageBox.warning(self, "Atención", "No hay clientes en la fila")
            self.lbl_resultado_atender.setText("Sin clientes atendidos recientemente.")
            return
            
        # Formateamos el texto incluyendo la duración exacta solicitada
        res_texto = (f"Atendido: Turno {datos_atencion['numero']}\n"
                     f"Llegada: {datos_atencion['llegada']}\n"
                     f"Salida: {datos_atencion['salida']}\n"
                     f"Duración: {datos_atencion['duracion']}")
        
        self.lbl_resultado_atender.setText(res_texto)
        
        # Refrescamos la lista de espera restante en pantalla
        self.lbl_resultado_turno.setText(self.simulador.obtener_cola_texto())

    def procesar_cierre(self):
        # 1. Al presionar cerrar, inmediatamente bloqueamos la entrada de nuevos clientes (cierre de puertas)
        self.btn_turno.setEnabled(False)
        self.txt_cliente.setEnabled(False)
        self.txt_cliente.setPlaceholderText("PUERTAS CERRADAS")

        # 2. Consultamos cómo está el estado de la cola
        resultado = self.simulador.cerrar_banco()
        
        if resultado["estado"] == "pendiente":
            # Avisamos que las puertas se cerraron pero hay rezagados que atender
            self.lbl_resultado_cerrar.setText(resultado["mensaje"])
            QMessageBox.warning(
                self, 
                "Puertas Cerradas", 
                "Se ha cerrado el ingreso de nuevos clientes. Por favor, termine de atender a los turnos que quedaron en espera."
            )
        else:
            # Si ya se vació, mostramos las estadísticas definitivas
            res_texto = (f"Clientes Atendidos: {resultado['atendidos']}\n"
                         f"Tiempo Promedio: {resultado['promedio']}")
            self.lbl_resultado_cerrar.setText(res_texto)
            
            # Bloqueamos el resto de los botones (Cierre absoluto de la ventanilla)
            self.btn_atender.setEnabled(False)
            self.btn_cerrar.setEnabled(False)
            
            QMessageBox.information(self, "Ventanilla Cerrada", "Cierre de caja total efectuado con éxito.")