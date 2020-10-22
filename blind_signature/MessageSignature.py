from PyQt5.QtWidgets import QWidget, QLabel


class MessageSignature(QWidget):
    def __init__(self, message, signature, status):
        super().__init__()

        self.message = message
        self.signature = signature
        self.status = status
        self.init_ui()

    def init_ui(self):
        label = QLabel('Check signature', self)
        label.move(100, 20)
        string_label = ' Message = ' + str(self.message) + ', Signature = ' + str(self.signature)

        message_signature = QLabel(str(string_label)[1: str(string_label).__len__() - 1], self)
        message_signature.move(100, 80)

        string_response = ' Signature ' + ('is authentic' if self.status else 'forged') + ' '
        status_response = QLabel(str(string_response)[1: str(string_response).__len__() - 1], self)
        status_response.move(100, 100)

        self.setGeometry(300, 300, 750, 400)
        self.setWindowTitle('Response')
        self.show()
