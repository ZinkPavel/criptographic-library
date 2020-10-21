from Crypto.Hash import SHA256


class Bulletin:
    def __init__(self, nominal):
        self.nominal = nominal
        self.signature = None
        self.f_n = int.from_bytes(SHA256.new(bytes(self.nominal, 'utf8')).digest(), 'big')

    def __str__(self):
        return '<' + str(self.nominal) + ', ' + str(self.signature) + '>'
