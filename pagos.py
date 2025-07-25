
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QFormLayout, QLineEdit, QPushButton,
    QComboBox, QTableWidget, QTableWidgetItem, QMessageBox
)
import db

class PagosTab(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        form_layout = QFormLayout()
        self.input_tipo = QComboBox()
        self.input_tipo.addItems(["empleado", "recibo"])
        self.input_descripcion = QLineEdit()
        self.input_monto = QLineEdit()

        form_layout.addRow("Tipo:", self.input_tipo)
        form_layout.addRow("Descripción:", self.input_descripcion)
        form_layout.addRow("Monto:", self.input_monto)

        btn_guardar = QPushButton("Registrar pago")
        btn_guardar.clicked.connect(self.guardar_pago)

        btn_mostrar = QPushButton("Mostrar pagos")
        btn_mostrar.clicked.connect(self.mostrar_pagos)

        self.tabla = QTableWidget()
        self.tabla.setColumnCount(4)
        self.tabla.setHorizontalHeaderLabels(["ID", "Tipo", "Descripción", "Monto"])

        layout.addLayout(form_layout)
        layout.addWidget(btn_guardar)
        layout.addWidget(btn_mostrar)
        layout.addWidget(self.tabla)

        self.setLayout(layout)

    def guardar_pago(self):
        tipo = self.input_tipo.currentText()
        descripcion = self.input_descripcion.text()
        monto = float(self.input_monto.text())

        conn = db.conectar()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO pagos (tipo, descripcion, monto) VALUES (?, ?, ?)",
                       (tipo, descripcion, monto))
        conn.commit()
        conn.close()

        QMessageBox.information(self, "Éxito", "Pago registrado.")
        self.input_descripcion.clear()
        self.input_monto.clear()

    def mostrar_pagos(self):
        conn = db.conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM pagos")
        pagos = cursor.fetchall()
        conn.close()

        self.tabla.setRowCount(0)
        for row_number, row_data in enumerate(pagos):
            self.tabla.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tabla.setItem(row_number, column_number, QTableWidgetItem(str(data)))
