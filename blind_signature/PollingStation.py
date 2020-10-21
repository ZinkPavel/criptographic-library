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

    def require(self, bulletin):
        bulletin.f_n = bulletin.f_n % self.N
        bulletin.signature = part_1.fast_modulo_exponentiation(bulletin.f_n, self.__c, self.N)

    def check(self, bulletin):
        f_n = int.from_bytes(SHA256.new(bytes(bulletin.nominal, 'utf8')).digest(), 'big') % self.N
        s_f = part_1.fast_modulo_exponentiation(bulletin.signature, self.d, self.N)

        return True if f_n == s_f else False
