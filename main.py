import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from interfaz import Ui_MainWindow  # Importa la clase generada por pyuic5

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Aquí puedes conectar señales y slots, y añadir lógica a tu aplicación
        # Por ejemplo:
        # self.ui.miBoton.clicked.connect(self.miFuncion)

    # def miFuncion(self):
    #     print("¡Botón presionado!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
