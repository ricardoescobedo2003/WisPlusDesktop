import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui_interfaz import Ui_Form  # Asegúrate de importar la clase generada

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()

        # Cargar la interfaz desde el archivo .ui
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Ui_Form()
    ventana.show()
    sys.exit(app.exec_())

