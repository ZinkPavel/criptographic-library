from PyQt5.QtWidgets import (QWidget, QCheckBox, QApplication,
                             QHBoxLayout, QVBoxLayout, QLabel, QButtonGroup, QAbstractButton, QPushButton)

from blind_signature.Bulletin import Bulletin


class UI(QWidget):

    def __init__(self):
        super().__init__()

        self.response = None
        self.bulletin = None
        self.initUI()

    def initUI(self):
        qa = QLabel('Согласны ли вы с поправками в коституцию?', self)
        checkBox1 = QCheckBox('За', self)
        checkBox2 = QCheckBox('Против', self)
        checkBox3 = QCheckBox('Воздрежусь', self)
        btn = QPushButton('Отправить', self)

        qa.move(85, 20)
        checkBox1.move(80, 80)
        checkBox2.move(180, 80)
        checkBox3.move(270, 80)

        group = QButtonGroup(self)
        group.addButton(checkBox1)
        group.addButton(checkBox2)
        group.addButton(checkBox3)

        group.buttonClicked.connect(self.changeText)

        btn.clicked.connect(self.reaction)
        btn.resize(btn.sizeHint())
        btn.move(180, 200)

        self.move(800, 500)
        self.setGeometry(300, 300, 450, 400)
        self.setWindowTitle('Bulletin')
        self.show()

        if btn.clicked:
            return self.bulletin

    def changeText(self, btn):
        self.response = btn.text()

    def reaction(self):
        print(type(self.response))
        self.bulletin = Bulletin(str(self.response))
        self.close()

