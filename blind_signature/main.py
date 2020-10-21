import sys

from PyQt5.QtWidgets import QApplication

from blind_signature.MessageSignature import MessageSignature
from blind_signature.PollingStation import PollingStation
from blind_signature.ui import UI


def main():
    app = QApplication(sys.argv)
    ui = UI()
    tmp = ui
    if app.exec():
        print(tmp.bulletin)

    response = tmp.bulletin
    print(type(response))

    pl = PollingStation()
    pl.require(response)
    #
    app2 = QApplication(sys.argv)
    check = pl.check(response)
    ui2 = MessageSignature(response.nominal, response.signature, check)
    sys.exit(app2.exec_())


if __name__ == "__main__":
    main()
