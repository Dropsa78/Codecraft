from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QFormLayout, QLineEdit,
    QPushButton, QTableWidget, QTableWidgetItem, QMessageBox, QHeaderView
)
import db

class EmpleadosTab(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        form_layout = QFormLayout()
        self.input_nombre = QLineEdit()
        self.input_puesto = QLineEdit()
        self.input_salario = QLineEdit()

        form_layout.addRow("Nombre:", self.input_nombre)
        form_layout.addRow("Puesto:", self.input_puesto)
        form_layout.addRow("Salario:", self.input_salario)

        btn_guardar = QPushButton("Guardar empleado")
        btn_guardar.clicked.connect(self.guardar_empleado)

        btn_mostrar = QPushButton("Mostrar empleados")
        btn_mostrar.clicked.connect(self.mostrar_empleados)

        self.tabla_empleados = QTableWidget()
        self.tabla_empleados.setColumnCount(5)  # id, nombre, puesto, salario, eliminar
        self.tabla_empleados.setHorizontalHeaderLabels(["ID", "Nombre", "Puesto", "Salario", "Eliminar"])
        self.tabla_empleados.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        layout.addLayout(form_layout)
        layout.addWidget(btn_guardar)
        layout.addWidget(btn_mostrar)
        layout.addWidget(self.tabla_empleados)

        self.setLayout(layout)

    def guardar_empleado(self):
        nombre = self.input_nombre.text()
        puesto = self.input_puesto.text()
        salario_texto = self.input_salario.text()

        if not nombre or not puesto or not salario_texto:
            QMessageBox.warning(self, "Error", "Todos los campos son obligatorios.")
            return

        try:
            salario = float(salario_texto)
        except ValueError:
            QMessageBox.warning(self, "Error", "El salario debe ser un número.")
            return

        db.insertar_empleado(nombre, puesto, salario)
        QMessageBox.information(self, "Éxito", f"Empleado {nombre} registrado.")
        self.input_nombre.clear()
        self.input_puesto.clear()
        self.input_salario.clear()
        self.mostrar_empleados()

    def mostrar_empleados(self):
        datos = db.obtener_empleados()
        self.tabla_empleados.setRowCount(0)

        for i, fila in enumerate(datos):
            self.tabla_empleados.insertRow(i)
            for j, valor in enumerate(fila):
                self.tabla_empleados.setItem(i, j, QTableWidgetItem(str(valor)))

            # Botón eliminar por registro
            btn_eliminar = QPushButton("Eliminar")
            btn_eliminar.clicked.connect(lambda checked, id=fila[0]: self.eliminar_empleado(id))
            self.tabla_empleados.setCellWidget(i, 4, btn_eliminar)

    def eliminar_empleado(self, id):
        confirmacion = QMessageBox.question(self, "Confirmar eliminación",
                                            f"¿Seguro que deseas eliminar al empleado con ID {id}?",
                                            QMessageBox.Yes | QMessageBox.No)
        if confirmacion == QMessageBox.Yes:
            db.eliminar_empleado(id)
            QMessageBox.information(self, "Eliminado", f"Empleado con ID {id} eliminado correctamente.")
            self.mostrar_empleados()
