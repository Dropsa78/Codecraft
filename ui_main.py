from PyQt5.QtWidgets import QMainWindow, QTabWidget, QPushButton, QVBoxLayout, QWidget, QLabel, QSpacerItem, QSizePolicy
from PyQt5.QtCore import Qt
from empleados import EmpleadosTab
from ventas import VentasTab
from devoluciones import DevolucionesTab
from productos import ProductosTab
from pagos import PagosTab
import exportar

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PYMES_APP")
        self.setGeometry(100, 100, 800, 600)

        # Layout principal
        main_widget = QWidget()
        main_layout = QVBoxLayout()

        # Título grande y centrado
        titulo = QLabel("CODECRAFT_APP")
        titulo.setAlignment(Qt.AlignCenter)
        titulo.setStyleSheet("font-size: 32px; font-weight: bold; margin-bottom: 20px;")
        main_layout.addWidget(titulo)

        # Espaciador
        main_layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Tabs
        tabs = QTabWidget()
        tabs.addTab(EmpleadosTab(), "Empleados")
        tabs.addTab(VentasTab(), "Ventas")
        tabs.addTab(DevolucionesTab(), "Devoluciones")
        tabs.addTab(ProductosTab(), "Productos")
        tabs.addTab(PagosTab(), "Pagos")

        main_layout.addWidget(tabs)

        # Espaciador
        main_layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Botón global de exportación con estilo
        btn_exportar_todo = QPushButton("Exportar TODO a Excel")
        btn_exportar_todo.setStyleSheet(
            "background-color: #4CAF50; color: white; font-size: 18px; padding: 10px 20px; border-radius: 8px;"
        )
        btn_exportar_todo.clicked.connect(self.exportar_todo)
        main_layout.addWidget(btn_exportar_todo, alignment=Qt.AlignCenter)

        main_widget.setLayout(main_layout) #qu eno abre el pto excel
        self.setCentralWidget(main_widget)

    def exportar_todo(self):
        exportar.exportar_todo("PYMESExcel.xlsx")
