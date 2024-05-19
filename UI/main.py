import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from panel import Ui_MainWindow  # Asegúrate de importar la clase generada

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()

        # Cargar la interfaz desde el archivo .ui
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = MiVentana()
    ventana.show()
    sys.exit(app.exec_())
