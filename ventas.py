# ventas.py
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QFormLayout, QLineEdit, QPushButton,
    QTableWidget, QTableWidgetItem, QMessageBox, QLabel
)
import db
import sqlite3

class VentasTab(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Formulario
        form_layout = QFormLayout()
        self.input_producto = QLineEdit()
        self.input_cantidad = QLineEdit()
        self.input_precio = QLineEdit()

        form_layout.addRow("Producto:", self.input_producto)
        form_layout.addRow("Cantidad:", self.input_cantidad)
        form_layout.addRow("Precio Unitario:", self.input_precio)

        btn_guardar = QPushButton("Registrar venta")
        btn_guardar.clicked.connect(self.guardar_venta)

        btn_mostrar = QPushButton("Mostrar ventas")
        btn_mostrar.clicked.connect(self.mostrar_ventas)

        self.label_total = QLabel("Total ventas: $0.00")

        # Tabla
        self.tabla = QTableWidget()
        self.tabla.setColumnCount(4)
        self.tabla.setHorizontalHeaderLabels(["ID", "Producto", "Cantidad", "Total"])

        # Layout general
        layout.addLayout(form_layout)
        layout.addWidget(btn_guardar)
        layout.addWidget(btn_mostrar)
        layout.addWidget(self.tabla)
        layout.addWidget(self.label_total)

        self.setLayout(layout)

    def guardar_venta(self):
        producto = self.input_producto.text()
        cantidad = int(self.input_cantidad.text())
        precio = float(self.input_precio.text())
        total = cantidad * precio

        conn = db.conectar()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO ventas (producto, cantidad, precio_unitario, total) VALUES (?, ?, ?, ?)",
                       (producto, cantidad, precio, total))
        conn.commit()
        conn.close()

        QMessageBox.information(self, "Éxito", "Venta registrada.")
        self.input_producto.clear()
        self.input_cantidad.clear()
        self.input_precio.clear()

    def mostrar_ventas(self):
        conn = db.conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM ventas")
        ventas = cursor.fetchall()
        conn.close()

        self.tabla.setRowCount(0)
        total_ventas = 0

        for row_number, row_data in enumerate(ventas):
            self.tabla.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tabla.setItem(row_number, column_number, QTableWidgetItem(str(data)))
            total_ventas += row_data[4]

        self.label_total.setText(f"Total ventas: ${total_ventas:.2f}")
