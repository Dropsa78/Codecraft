from PyQt5.QtWidgets import QMainWindow, QTabWidget, QPushButton, QVBoxLayout, QWidget
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

        # Tabs
        tabs = QTabWidget()
        tabs.addTab(EmpleadosTab(), "Empleados")
        tabs.addTab(VentasTab(), "Ventas")
        tabs.addTab(DevolucionesTab(), "Devoluciones")
        tabs.addTab(ProductosTab(), "Productos")
        tabs.addTab(PagosTab(), "Pagos")

        main_layout.addWidget(tabs)

        # Botón global de exportación
        btn_exportar_todo = QPushButton("Exportar TODO a Excel")
        btn_exportar_todo.clicked.connect(self.exportar_todo)
        main_layout.addWidget(btn_exportar_todo)

        main_widget.setLayout(main_layout) #qu eno abre el pto excel
        self.setCentralWidget(main_widget)

    def exportar_todo(self):
        exportar.exportar_todo("PYMESExcel.xlsx")
