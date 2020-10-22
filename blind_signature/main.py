import sys

from PyQt5.QtWidgets import QApplication

from blind_signature.MessageSignature import MessageSignature
from blind_signature.PollingStation import PollingStation
from blind_signature.ui import UI


def main():
    app_1 = QApplication(sys.argv)
    ui = UI()

    if app_1.exec():
        print(ui.bulletin)

    response = ui.bulletin

    ps = PollingStation()
    ps.require(response)

    app_2 = QApplication(sys.argv)
    check = ps.check(response)
    ui_2 = MessageSignature(response.nominal, response.signature, check)

    sys.exit(app_2.exec_())


if __name__ == "__main__":
    main()
