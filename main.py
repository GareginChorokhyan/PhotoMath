from Controller.Controller import Controller
import sys
from PySide6.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication(sys.argv)
    controller = Controller()
    controller.run()
    sys.exit(app.exec())


