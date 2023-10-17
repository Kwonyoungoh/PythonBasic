import sys
from PySide6.QtWidgets import QApplication,QWidget,QPushButton
from PySide6.QtGui import QIcon
from PySide6.QtCore import QCoreApplication
class myApp(QWidget):

    def __init__(self):
        super().__init__()
        self.btn1 = QPushButton('quit',self)
        self.init_ui()


    def init_ui(self):

        self.btn1.move(50,50)
        self.btn1.resize(self.btn1.sizeHint())

        self.setWindowTitle('my first')
        self.setWindowIcon(QIcon('q_icon.png'))
        self.move(300,400)
        self.resize(400,200)

        self.btn1.clicked.connect(QCoreApplication.instance().quit)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = myApp()
    sys.exit(app.exec())