from PyQt5.QtWidgets import QApplication
from ui_main import MainWindow
from db import crear_tablas
import sys

if __name__ == "__main__":
    crear_tablas()  
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    