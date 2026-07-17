from PyQt5.QtWidgets import QDialog, QTableWidgetItem, QMessageBox
from PyQt5.uic import loadUi
from aplicaciones.lista_impresion import GestorImpresion

class MenuImpresora(QDialog):
    def __init__(self):
        super().__init__()
        # Carga la interfaz gráfica de Qt Designer
        loadUi("ui/impresora.ui", self)
        
        # Instancia la lógica
        self.gestor = GestorImpresion()
        
        # Conexiones de los botones
        self.btn_agregar.clicked.connect(self.ejecutar_agregar)
        self.btn_imprimir.clicked.connect(self.ejecutar_imprimir)
        self.btn_frente.clicked.connect(self.ejecutar_consultar_frente)
        
        # Inicializa las cabeceras de la tabla
        self.tbl_pendientes.setColumnCount(4)
        self.tbl_pendientes.setHorizontalHeaderLabels(["ID", "Usuario", "Documento", "Páginas"])
        self.actualizar_interfaz()

    def actualizar_interfaz(self):
        pendientes = self.gestor.obtener_lista_pendientes()
        total = self.gestor.obtener_total_pendientes()
        
        # Actualiza el total (Size)
        self.lbl_total_pendientes.setText(f"Trabajos en cola (Size): {total}")
        
        # Renderiza en la tabla
        self.tbl_pendientes.setRowCount(0)
        for i, trabajo in enumerate(pendientes):
            self.tbl_pendientes.insertRow(i)
            self.tbl_pendientes.setItem(i, 0, QTableWidgetItem(str(trabajo.consecutivo)))
            self.tbl_pendientes.setItem(i, 1, QTableWidgetItem(trabajo.usuario))
            self.tbl_pendientes.setItem(i, 2, QTableWidgetItem(trabajo.documento))
            self.tbl_pendientes.setItem(i, 3, QTableWidgetItem(str(trabajo.paginas)))

    def ejecutar_agregar(self):
        usuario = self.txt_usuario.text()
        documento = self.txt_documento.text()
        paginas = self.spin_paginas.value()
        
        try:
            trabajo = self.gestor.agregar_trabajo(usuario, documento, paginas)
            self.txt_usuario.clear()
            self.txt_documento.clear()
            self.spin_paginas.setValue(1)
            
            self.lbl_mensajes.setText(f"[ÉXITO] Trabajo agregado: {trabajo}")
            self.actualizar_interfaz()
        except ValueError as e:
            QMessageBox.warning(self, "Error de Validación", str(e))

    def ejecutar_imprimir(self):
        try:
            trabajo_procesado = self.gestor.imprimir_siguiente()
            self.lbl_mensajes.setText(f"[PROCESADO] {trabajo_procesado} se imprimió.")
            self.actualizar_interfaz()
        except IndexError as e:
            QMessageBox.critical(self, "Error de Cola", str(e))

    def ejecutar_consultar_frente(self):
        frente = self.gestor.ver_frente()
        if frente:
            self.lbl_mensajes.setText(f"[FRENTE] Siguiente en fila: {frente}")
            QMessageBox.information(self, "Siguiente en Fila", f"Trabajo en el frente:\n\n{frente}")
        else:
            QMessageBox.information(self, "Cola Vacía", "No hay trabajos pendientes.")