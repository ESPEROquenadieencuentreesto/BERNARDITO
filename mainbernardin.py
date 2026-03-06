import sys
from PySide6.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
from PySide6.QtGui import QFont, QIcon
from PySide6.QtCore import Qt
from qt_material import apply_stylesheet

def main():

    sys.argv += ['-style', 'Fusion']
    app = QApplication(sys.argv)
    apply_stylesheet(app, theme='dark_teal.xml')

    # Conf de la ventana
    window = QWidget()
    window.setWindowTitle('Bernardito Prueba 1')
    window.setMinimumSize(500, 450)
    
    window.setWindowIcon(QIcon("calzoskiadulto.jpg"))


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
