from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import QFontDatabase, QIcon
from .design import Ui_MainWindow
from PySide6.QtWidgets import *
from PySide6.QtCore import Qt


class View(QMainWindow):
    def __init__(self):
        super().__init__()
        self.fxPanel = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.len_temp = len(self.ui.label_temp.text())
        self.len_le = len(self.ui.le_entry.text())
        self.expression = ""
        self.entry_max_len = self.ui.le_entry.maxLength()

        QFontDatabase.addApplicationFont("data/ui/fonts/Rubik-Regular.ttf")

    def update_view(self, value):
        self.Show_text(value)

    def clear_entry(self):
        self.ui.le_entry.setText('0')

    def clear_le(self):
        self.ui.le_entry.clear()

    def clear_temp(self):
        self.ui.label_temp.clear()

    def clear_all(self):
        self.expression = '0'
        self.ui.le_entry.setText(self.expression)
        self.ui.label_temp.clear()

    def Show(self):
        self.show()

    def Show_text(self, text: str):
        self.ui.le_entry.setText(text)

    def Show_temp(self, text: str):
        self.ui.label_temp.setText(text)

    def create_fxPanel(self):
        buttons = []
        self.fxPanel = QWidget()
        self.fxPanel.setStyleSheet(self.styleSheet())
        self.fxPanel.setWindowIcon(QIcon(u":/icons/Downloads/_5fe58046-7e4c-4a4a-a920-a013dba99d18.ico"))
        self.fxPanel.setWindowTitle("F(X)")
        self.fxPanel.resize(300, 300)

        layout = QGridLayout()

        max_functions_per_row = 5

        functions = [
            "sin", "cos", "tan", "ctg",
            "sinh", "cosh", "tanh", "ctgh",
            "arcsin", "arccos", "arctan", "arcctg",
            "ln", "log", "exp", "logy",
            "abs", "ceil", "floor", "round",
            "yroot", "factorial", "deg", "rad", "mod",
        ]

        num_functions = len(functions)
        grid_size = (num_functions + max_functions_per_row - 1) // max_functions_per_row

        for row in range(grid_size):
            for col in range(max_functions_per_row):
                index = row * max_functions_per_row + col
                if index < num_functions:
                    func_name = functions[index]
                    button = QPushButton(func_name.capitalize())
                    button.setFixedSize(71, 87)
                    button.setCursor(Qt.OpenHandCursor)
                    button.setText(func_name)

                    # # Load icon for the specific button
                    # if func_name == "yroot":
                    #     icon1 = QIcon()
                    #     icon1.addFile(u":/icons/Downloads/square-root.png", QSize(), QIcon.Normal, QIcon.Off)
                    #     button.setIcon(icon1)
                    #     button.setIconSize(QSize(24, 24))
                    #     button.setText("")

                    if func_name == "factorial":
                        button.setText(u"fact")

                    layout.addWidget(button, row, col)
                    buttons.append(button)
                    # Connect buttons to calculation methods
                    # button

        self.fxPanel.setWindowModality(Qt.WindowModal)
        self.fxPanel.setLayout(layout)
        self.fxPanel.show()
        return buttons

    def closeEvent(self, event):
        if hasattr(self, 'fxPanel') and isinstance(self.fxPanel, QWidget):
            self.fxPanel.close()
        event.accept()
