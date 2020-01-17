import sys
from PySide2.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QLineEdit, QPushButton

class Form(QWidget):
    def __init__(self,parent = None):
        super(Form, self).__init__(parent)
        self.setWindowTitle("My Form")
        self.resize(250, 150)
        self.move(300, 300)
        self.label = QLabel("Привет, можешь сложить два числа!")
        self.edit1 = QLineEdit()
        self.edit2 = QLineEdit()
        self.button = QPushButton("Расчитать")
        self.answer = QLabel("Здесь будет ваш ответ")


        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.edit1)
        layout.addWidget(self.edit2)
        layout.addWidget(self.answer)
        layout.addWidget(self.button)
        self.setLayout(layout)

        self.button.clicked.connect(self.getAns)

    def getAns(self):
        self.answer.setText('Ваш ответ: {}'.format(int(self.edit1.text()) + int(self.edit2.text())))

if __name__ == '__main__':
    app = QApplication()

    form = Form()
    form.show()

    sys.exit(app.exec_())