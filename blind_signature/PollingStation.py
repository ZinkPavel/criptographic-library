from Crypto.Hash import SHA256

import part_1
import part_3


class PollingStation:
    def __init__(self):
        self.__p = part_1.gen_p()
        self.__q = part_1.gen_p()
        self.__c = part_1.gen_p()

        self.N = self.__p * self.__q
        self.d = part_3.modulo_inversion(self.__c, (self.__p - 1) * (self.__q - 1))

    def require(self, bill):
        bill.f_n = bill.f_n % self.N
        bill.signature = part_1.fast_modulo_exponentiation(bill.f_n, self.__c, self.N)

    def check(self, bill):
        f_n = int.from_bytes(SHA256.new(bytes(bill.nominal)).digest(), 'big') % self.N
        s_f = part_1.fast_modulo_exponentiation(bill.signature, self.d, self.N)

        return True if f_n == s_f else False
