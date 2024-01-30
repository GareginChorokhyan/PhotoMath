from PySide6.QtCore import Slot
from Model.Voice import Audio
from Model.VirtualCalculator import VirtualCalculator
from functools import partial
from Model.Expression import Expression
from View.View import View

OPERATIONS = {
    'btn_plus': '+',
    'btn_sub': '-',
    'btn_mull': '*',
    'btn_div': '/',
    'btn_mod': '%',
    'btn_pow': '^',
}


class Controller:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.initialized = True
            self.model = Expression()
            self.view = View()
            self.camera = VirtualCalculator()
            self.voice = Audio()

    @staticmethod
    def get_instance():
        return Controller._instance

    def run(self):
        self.view.Show()
        self.initConnections()

    @Slot()
    def handle_camera(self):
        self.camera.run()

    def handle_open_parentheses(self):
        self.view.Show_text(self.model.add_open_parentheses())

    def handle_pi(self):
        self.view.Show_text(self.model.add_pi())

    def handle_e(self):
        self.view.Show_text(self.model.add_e())

    def handle_text(self):
        self.view.Show_text(self.model.backspace_entry())

    def handle_sqrt(self):
        self.view.Show_text(self.model.sqrt_symbol())

    def handle_close_parentheses(self):
        self.view.Show_text(self.model.add_close_parentheses())

    def handle_button_click(self, digit):
        self.view.Show_text(self.model.add_digit(str(digit)))

    def handle_point_click(self):
        self.view.Show_text(self.model.add_point())

    def handle_app(self):
        self.view.Show_text(self.model.add_app())

    def handle_button_audio(self):
        self.view.clear_temp()
        self.view.clear_entry()
        result = self.voice.audio()
        self.view.clear_le()
        self.view.Show_text(str(result))

    def handle_clear_click(self):
        self.model.clear()
        self.view.clear_all()

    def handle_operation_click(self, operation):
        if self.view.len_temp != 0:
            self.view.clear_temp()  # Clear the label_temp in the view
            self.model.exp = ""
        if operation in OPERATIONS:
            self.model.add_operations(OPERATIONS[operation])
            self.view.Show_text(self.model.exp)  # Update view with the current expression
        else:
            print("Invalid operation")

    def handle_percentage_click(self):
        result = self.model.add_percentage()
        if result is not None:
            self.view.Show_text(self.model.exp)
        else:
            print("Invalid operation")

    def handle_equal_click(self):
        result = self.model.calculate()
        if result is not None:
            self.view.Show_temp(f"{self.model.current_exp} =")
            self.view.Show_text(str(result))
        else:
            self.view.Show_temp("Invalid Expression")
            self.view.clear_entry()

    def handle_fx(self):
        buttons = self.view.create_fxPanel()  # Assuming create_fxPanel returns a list of buttons

        def attach_handler(btn, txt):
            btn.clicked.connect(lambda: self.view.Show_text(self.model.add_math_operations(txt)))

        for button in buttons:
            text = button.text()
            attach_handler(button, text)

    def initConnections(self):
        for i in range(10):
            button = getattr(self.view.ui, f"btn_{i}")
            button.clicked.connect(partial(self.handle_button_click, i))

        for btn_name in OPERATIONS:
            op = getattr(self.view.ui, btn_name)
            op.clicked.connect(partial(self.handle_operation_click, btn_name))

        self.view.ui.btn_equal.clicked.connect(self.handle_equal_click)
        self.view.ui.btn_sqrt.clicked.connect(self.handle_sqrt)
        self.view.ui.btn_Left.clicked.connect(self.handle_open_parentheses)
        self.view.ui.btn_Right.clicked.connect(self.handle_close_parentheses)
        self.view.ui.btn_clear.clicked.connect(self.handle_clear_click)
        self.view.ui.btn_clearEntry.clicked.connect(self.view.clear_entry)
        self.view.ui.btn_camera.clicked.connect(self.handle_camera)
        self.view.ui.btn_mikro.clicked.connect(self.handle_button_audio)
        self.view.ui.btn_point.clicked.connect(self.handle_point_click)
        self.view.ui.btn_mod.clicked.connect(self.handle_percentage_click)
        self.view.ui.btn_fx.clicked.connect(self.handle_fx)
        self.view.ui.btn_backspace.clicked.connect(self.handle_text)
        self.view.ui.btn_pi.clicked.connect(self.handle_pi)
        self.view.ui.btn_e.clicked.connect(self.handle_e)
        self.view.ui.btn_a.clicked.connect(self.handle_app)
