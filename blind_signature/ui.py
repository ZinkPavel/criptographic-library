from PyQt5.QtWidgets import (QWidget, QCheckBox, QLabel, QButtonGroup, QPushButton)

from blind_signature.Bulletin import Bulletin


class UI(QWidget):
    def __init__(self):
        super().__init__()

        self.response = None
        self.bulletin = None
        self.init_ui()

    def init_ui(self):
        qa = QLabel('HTML a programming language ?', self)
        check_box_1 = QCheckBox('Yes', self)
        check_box_2 = QCheckBox('No', self)
        check_box_3 = QCheckBox('Refrain', self)
        btn = QPushButton('Send', self)

        qa.move(85, 20)
        check_box_1.move(80, 80)
        check_box_2.move(180, 80)
        check_box_3.move(270, 80)

        group = QButtonGroup(self)
        group.addButton(check_box_1)
        group.addButton(check_box_2)
        group.addButton(check_box_3)

        group.buttonClicked.connect(self.change_text)

        btn.clicked.connect(self.reaction)
        btn.resize(btn.sizeHint())
        btn.move(180, 200)

        self.move(800, 500)
        self.setGeometry(300, 300, 450, 400)
        self.setWindowTitle('Bulletin')
        self.show()

        if btn.clicked:
            return self.bulletin

    def change_text(self, btn):
        self.response = btn.text()

    def reaction(self):
        self.bulletin = Bulletin(str(self.response))
        self.close()

