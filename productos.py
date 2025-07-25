# productos.py
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QFormLayout, QLineEdit, QPushButton,
    QTableWidget, QTableWidgetItem, QMessageBox
)
import db

class ProductosTab(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        form_layout = QFormLayout()
        self.input_nombre = QLineEdit()
        self.input_stock = QLineEdit()
        self.input_precio = QLineEdit()

        form_layout.addRow("Nombre:", self.input_nombre)
        form_layout.addRow("Stock:", self.input_stock)
        form_layout.addRow("Precio:", self.input_precio)

        btn_guardar = QPushButton("Registrar producto")
        btn_guardar.clicked.connect(self.guardar_producto)

        btn_mostrar = QPushButton("Mostrar productos")
        btn_mostrar.clicked.connect(self.mostrar_productos)

        self.tabla = QTableWidget()
        self.tabla.setColumnCount(4)
        self.tabla.setHorizontalHeaderLabels(["ID", "Nombre", "Stock", "Precio"])

        layout.addLayout(form_layout)
        layout.addWidget(btn_guardar)
        layout.addWidget(btn_mostrar)
        layout.addWidget(self.tabla)

        self.setLayout(layout)

    def guardar_producto(self):
        nombre = self.input_nombre.text()
        stock = int(self.input_stock.text())
        precio = float(self.input_precio.text())

        conn = db.conectar()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO productos (nombre, stock, precio) VALUES (?, ?, ?)",
                       (nombre, stock, precio))
        conn.commit()
        conn.close()

        QMessageBox.information(self, "Éxito", "Producto registrado.")
        self.input_nombre.clear()
        self.input_stock.clear()
        self.input_precio.clear()

    def mostrar_productos(self):
        conn = db.conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM productos")
        productos = cursor.fetchall()
        conn.close()

        self.tabla.setRowCount(0)
        for row_number, row_data in enumerate(productos):
            self.tabla.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tabla.setItem(row_number, column_number, QTableWidgetItem(str(data)))
