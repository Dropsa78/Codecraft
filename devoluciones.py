# devoluciones.py
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QFormLayout, QLineEdit, QPushButton,
    QTableWidget, QTableWidgetItem, QMessageBox, QLabel, QComboBox
)
import db

class DevolucionesTab(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        form_layout = QFormLayout()
        self.input_tipo = QComboBox()
        self.input_tipo.addItems(["cliente", "proveedor"])
        self.input_producto = QLineEdit()
        self.input_cantidad = QLineEdit()
        self.input_motivo = QLineEdit()

        form_layout.addRow("Tipo:", self.input_tipo)
        form_layout.addRow("Producto:", self.input_producto)
        form_layout.addRow("Cantidad:", self.input_cantidad)
        form_layout.addRow("Motivo:", self.input_motivo)

        btn_guardar = QPushButton("Registrar devolución")
        btn_guardar.clicked.connect(self.guardar_devolucion)

        btn_mostrar = QPushButton("Mostrar devoluciones")
        btn_mostrar.clicked.connect(self.mostrar_devoluciones)

        self.tabla = QTableWidget()
        self.tabla.setColumnCount(5)
        self.tabla.setHorizontalHeaderLabels(["ID", "Tipo", "Producto", "Cantidad", "Motivo"])

        layout.addLayout(form_layout)
        layout.addWidget(btn_guardar)
        layout.addWidget(btn_mostrar)
        layout.addWidget(self.tabla)

        self.setLayout(layout)

    def guardar_devolucion(self):
        tipo = self.input_tipo.currentText()
        producto = self.input_producto.text()
        cantidad = int(self.input_cantidad.text())
        motivo = self.input_motivo.text()

        conn = db.conectar()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO devoluciones (tipo, producto, cantidad, motivo) VALUES (?, ?, ?, ?)",
                       (tipo, producto, cantidad, motivo))
        conn.commit()
        conn.close()

        QMessageBox.information(self, "Éxito", "Devolución registrada.")
        self.input_producto.clear()
        self.input_cantidad.clear()
        self.input_motivo.clear()

    def mostrar_devoluciones(self):
        conn = db.conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM devoluciones")
        devoluciones = cursor.fetchall()
        conn.close()

        self.tabla.setRowCount(0)
        for row_number, row_data in enumerate(devoluciones):
            self.tabla.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tabla.setItem(row_number, column_number, QTableWidgetItem(str(data)))
