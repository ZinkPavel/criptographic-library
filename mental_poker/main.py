from mental_poker.PokerRoom import PokerRoom


def main():
    instance = PokerRoom(5)
    instance.distribution()
    print(instance)


if __name__ == "__main__":
    main()
