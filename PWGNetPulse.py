import sys
import platform
import os
from PySide6.QtWidgets import QApplication, QWidget, QStackedWidget,QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton
from PySide6.QtGui import QFont, QIcon, QFontDatabase
from PySide6.QtCore import Qt

USERS = {
    "pedrito": "1234",
}

TEMAS = {
    "oscuro": { "bg": "#000000", "card": "#000000", "accent": "#ffffff", "text_dim": "#555555", "input_bg": "#1a1a1a", "label_fix": "#ffffff"
    },
    "claro": { "bg": "#f0f0f0", "card": "#ffffff", "accent": "#000000", "text_dim": "#999999", "input_bg": "#e0e0e0", "label_fix": "#000000"
    },
}
tema_actual = "oscuro"
ERROR = "#ff4444"

class LoginScreen(QWidget):
    def __init__(self, on_success):
        super().__init__()
        self.on_success = on_success
        self._build()

    def _build(self):
        root = QVBoxLayout(self)
        root.setContentsMargins(0, 0, 0, 0)

        self.card = QWidget()
        self.card.setFixedWidth(380)
        self.card.setStyleSheet(f"""
            QWidget {{
                background-color: #000000;
                border-radius: 14px;
                border: 1px solid #ffffff;
            }}
        """)
        cl = QVBoxLayout(self.card)
        cl.setContentsMargins(36, 40, 36, 40)
        cl.setSpacing(0)

        self.title = QLabel("PWGNetPulse")
        self.title.setFont(QFont("Michroma", QFont.Bold))
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setStyleSheet(f"color: #ffffff; border: none; font-size: 31px;")
        cl.addWidget(self.title)

        self.sub = QLabel("Inicia sesión para continuar")
        self.sub.setFont(QFont("Consolas", 9))
        self.sub.setAlignment(Qt.AlignCenter)
        self.sub.setStyleSheet(f"color: #ffffff; border: none; margin-bottom: 45px;")
        cl.addWidget(self.sub)

        self.lbl_usuario = self._label("USUARIO")
        cl.addWidget(self.lbl_usuario)
        self.inp_user = self._input("tu_usuario")
        cl.addWidget(self.inp_user) 
        cl.addSpacing(14)

        self.lbl_pass = self._label("CONTRASEÑA")
        cl.addWidget(self.lbl_pass)
        self.inp_pass = self._input("********", password=True)
        cl.addWidget(self.inp_pass)
        cl.addSpacing(8)

        self.lbl_error = QLabel("")
        self.lbl_error.setFont(QFont("Consolas", 9))
        self.lbl_error.setAlignment(Qt.AlignCenter)
        self.lbl_error.setFixedHeight(20)
        self.lbl_error.setStyleSheet(f"color: {ERROR}; border: none;")
        cl.addWidget(self.lbl_error)
        cl.addSpacing(14)

        self.btn = QPushButton("ENTRAR")
        self.btn.setFont(QFont("Consolas", 10, QFont.Bold))
        self.btn.setFixedHeight(44)
        self.btn.setCursor(Qt.PointingHandCursor)
        self.btn.setStyleSheet(f"""
            QPushButton {{
                background-color: #1a1a1a;
                color: #ffffff;
                border: none;
                border-radius: 8px;
                letter-spacing: 3px;
            }}
            QPushButton:hover {{ background-color: #ffffff; color: #000000 }}
            QPushButton:pressed {{ background-color: 0d0d0d; }}
        """)
        self.btn.clicked.connect(self._check)
        cl.addWidget(self.btn)

        self.inp_pass.returnPressed.connect(self._check)
        self.inp_user.returnPressed.connect(self._check)

        row = QHBoxLayout()
        row.addStretch()
        row.addWidget(self.card)
        row.addStretch()

        root.addStretch()
        root.addLayout(row)
        root.addStretch()

    def _label(self, text):
        lbl = QLabel(text)
        lbl.setFont(QFont("Consolas", 8, QFont.Bold))
        lbl.setStyleSheet(f"color: #ffffff; border: none; margin-bottom: 4px; letter-spacing: 2px;")
        return lbl

    def _input(self, placeholder, password=False):
        inp = QLineEdit()
        inp.setPlaceholderText(placeholder)
        inp.setFont(QFont("Consolas", 11))
        inp.setFixedHeight(40)
        if password:
            inp.setEchoMode(QLineEdit.Password)
        inp.setStyleSheet(f"""
            QLineEdit {{
                background-color: #1a1a1a;
                color: #fff;
                border: 1px solid #ffffff;
                border-radius: 8px;
                padding: 0 12px;
            }}
            QLineEdit:focus {{ border: 1px solid #ffffff; }}
        """)
        return inp

    def _check(self):
        user = self.inp_user.text().strip().lower()
        pwd  = self.inp_pass.text()

        if USERS.get(user) == pwd:
            self.lbl_error.setText("")
            self.on_success()
        else:
            self.lbl_error.setText("Usuario o contraseña incorrectos")

    def aplicar_tema(self, t):
        self.card.setStyleSheet(f""" QWidget {{ background-color: {t['card']}; border-radius: 14px; border: 1px solid {t['accent']}; }} """)
        self.title.setStyleSheet(f"color: {t['accent']}; border: none; font-size: 31px;")
        self.sub.setStyleSheet(f"color: {t['accent']}; border: none; margin-bottom: 45px;")
        self.inp_user.setStyleSheet(self._input_style(t))
        self.inp_pass.setStyleSheet(self._input_style(t))
        
        color_label = f"color: {t['label_fix']}; border: none; margin-bottom: 4px; letter-spacing: 2px;"
        self.lbl_usuario.setStyleSheet(color_label)
        self.lbl_pass.setStyleSheet(color_label)

    def _input_style(self, t):
        return f"""
        QLineEdit {{ background-color: {t['input_bg']}; color: {t['accent']}; border: 1px solid {t['accent']}; border-radius: 8px; padding: 0 12px; }}
    """


class DashboardScreen(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        self.lbl = QLabel("Ola chikos")
        self.lbl.setFont(QFont("Consolas", 16, QFont.Bold))
        self.lbl.setAlignment(Qt.AlignCenter)
        self.lbl.setStyleSheet("color: #ffffff;")
        layout.addWidget(self.lbl)

    def aplicar_tema(self, t):
        self.setStyleSheet(f"background-color: {t['bg']};")
        self.lbl.setStyleSheet(f"color: {t['accent']};")


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PWGNetPulse")
        self.setMinimumSize(800, 700)

        if platform.system() == "Windows":
            import ctypes
            ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("pwg.netpulse")

        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        icon_path = os.path.join(BASE_DIR, "iconhub.jpg")
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))

        self.stack = QStackedWidget()
        self.login     = LoginScreen(on_success=self._go_to_dashboard)
        self.dashboard = DashboardScreen()

        self.stack.addWidget(self.login)      
        self.stack.addWidget(self.dashboard)
        self.stack.setCurrentIndex(0)   

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.stack)

        self.btn_tema = QPushButton("🌙", self)
        self.btn_tema.setFixedSize(36, 36)
        self.btn_tema.setCursor(Qt.PointingHandCursor)
        self.btn_tema.setStyleSheet("border: none; font-size: 18px; background: transparent;")
        self.btn_tema.clicked.connect(self._cambiar_tema)
        self._reposicionar_btn_tema()

    def _go_to_dashboard(self):
        self.stack.setCurrentIndex(1)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self._reposicionar_btn_tema()

    def _reposicionar_btn_tema(self):
        self.btn_tema.move(self.width() - 46, 10)

    def _cambiar_tema(self):
        global tema_actual
        tema_actual = "claro" if tema_actual == "oscuro" else "oscuro"
        t = TEMAS[tema_actual]
        self.btn_tema.setText("☀️" if tema_actual == "claro" else "🌙")
        self.setStyleSheet(f"background-color: {t['bg']}; color: {t['accent']};")
        self.login.aplicar_tema(t)
        self.dashboard.aplicar_tema(t)


def main():

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    ruta_fuente = os.path.join(BASE_DIR, "Michroma-Regular.ttf")
    if os.path.exists(ruta_fuente):
        QFontDatabase.addApplicationFont(ruta_fuente)
    else:
        print(f"Advertencia: No se encontró la fuente en {ruta_fuente}")

    sys.argv += ['-style', 'Fusion']
    app = QApplication(sys.argv)
    t = TEMAS[tema_actual]
    app.setStyleSheet(f"""
        QWidget {{ background-color: {t['bg']}; color: {t['accent']}; font-size: 13px; }}
    """)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()

