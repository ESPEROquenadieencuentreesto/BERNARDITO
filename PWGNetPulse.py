import sys
import platform
from PySide6.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
from PySide6.QtGui import QFont, QIcon
from PySide6.QtCore import Qt
from qt_material import apply_stylesheet

def main():

    if platform.system() == "Windows":
        import ctypes
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("bernardin.app")
    
    sys.argv += ['-style', 'Fusion']
    app = QApplication(sys.argv)
    app.setStyleSheet("""
    QWidget {
            background-color: #0d0d0d;
            color: #ffffff;
            font-size: 13px;
        }
        QLabel {
            color: #ffffff;
        }
    """)
    app.setWindowIcon(QIcon("iconhub.jpg"))

    # Conf de la ventana
    window = QWidget()
    window.setWindowTitle('PWGNetPulse')
    window.setMinimumSize(550, 500)
    


    # Layout y Texto
    layout = QVBoxLayout()
    label = QLabel(" Vienvenidos chikos! ")
    fuente = QFont("Firacode Nerd Font", 20, QFont.Bold) 
    label.setFont(fuente)
    label.setAlignment(Qt.AlignCenter)
    
    layout.addWidget(label)
    window.setLayout(layout)
    
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
