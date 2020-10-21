from blind_signature.Bulletin import Bulletin
from blind_signature.PollingStation import PollingStation


def main():
    station = PollingStation()
    bill = Bulletin(100)
    station.require(bill)
    print(station.check(bill))


if __name__ == "__main__":
    main()
