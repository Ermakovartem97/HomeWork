import sys
from PySide2.QtWidgets import QApplication, QWidget, QLabel, QGridLayout, QLineEdit, QPushButton

class Form(QWidget):
    def __init__(self,parent = None):
        super(Form, self).__init__(parent)
        self.setWindowTitle("My Form")
        self.resize(350, 250)
        self.move(300, 300)
        self.label = QLabel("Это мой калькулятор")
        self.b1 = QPushButton("1")
        self.b2 = QPushButton("2")
        self.button = QPushButton("=")
        self.answer = QLabel("Ответ")

        layout = QGridLayout()
        layout.addWidget(self.answer,1,0,0,0)
        layout.addWidget(self.label,0,0)
        layout.addWidget(self.b1,2,1)
        layout.addWidget(self.b2,2,2)
        layout.addWidget(self.button,3,0)
        self.setLayout(layout)

        self.button.clicked.connect(self.getAns)

    def getAns(self):
        self.answer.setText('Ваш ответ: {}'.format(int(self.b1.text()) + int(self.b2.text())))

if __name__ == '__main__':
    app = QApplication()

    form = Form()
    form.show()

    sys.exit(app.exec_())