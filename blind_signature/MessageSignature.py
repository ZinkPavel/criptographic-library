from PyQt5.QtWidgets import QWidget, QLabel


class MessageSignature(QWidget):

    def __init__(self, message, signature, status):
        super().__init__()

        self.message = message
        self.signature = signature
        self.status = status
        self.initUI()

    def initUI(self):
        label = QLabel('Проверка электронной подписи', self)
        label.move(100, 20)
        stringLabel = 'message = ', self.message, 'signature = ', self.signature
        print(stringLabel)
        messageSignature = QLabel(str(stringLabel)[1: str(stringLabel).__len__()-1], self)
        messageSignature.move(100, 80)

        stringResponse = 'Status =', self.status
        print(stringResponse)
        statusResponse = QLabel(str(stringResponse)[1: str(stringResponse).__len__()-1], self)
        statusResponse.move(100, 100)

        self.setGeometry(300, 300, 750, 400)
        self.setWindowTitle('Response')
        self.show()
