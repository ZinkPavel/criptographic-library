import sys
import random
import math
from Crypto.Hash import SHA256

import part_1


def gen_g(p):
    if not part_1.is_prime(p):
        print('GEN_G: \'p\' is not prime !')

    g = random.randint(1, p - 1)

    while part_1.fast_modulo_exponentiation(g, (p - 1) / 2, p) == 1:
        g = random.randint(1, p - 1)
    return g


# make non rand
def gen_coprime_integer_in_range(x, a, b):
    result = random.randint(a, b)
    while part_1.gcd(result, x)[0] != 1:
        result = random.randint(a, b)
    return result


def modulo_inversion(a, p):
    result = part_1.gcd(a, p)[2]
    if result < 0:
        result += p
    return result


class SignatureElGamal:
    def __init__(self, message):
        self.p = part_1.gen_p()
        self.g = gen_g(self.p)
        self.message = SHA256.new(message).digest()  # return

        self.x = random.randint(1, self.p - 1)
        self.open_key = part_1.fast_modulo_exponentiation(self.g, self.x, self.p)
        self.k = gen_coprime_integer_in_range(self.p - 1, 1, self.p - 1)
        self.r = part_1.fast_modulo_exponentiation(self.g, self.k, self.p)  # return

        self.u = 0
        self.s = 0  # return

    def encode(self):
        hash_f = int.from_bytes(self.message, 'big') % self.p
        self.u = (hash_f - self.x * self.r) % (self.p - 1)
        self.s = modulo_inversion(self.k, (self.p - 1)) * self.u % (self.p - 1)

    def decode(self):
        hash_f = int.from_bytes(self.message, 'big') % self.p
        lhs = (part_1.fast_modulo_exponentiation(self.open_key, self.r, self.p) * part_1.fast_modulo_exponentiation(self.r, self.s, self.p)) % self.p
        rhs = part_1.fast_modulo_exponentiation(self.g, hash_f, self.p)

        if lhs != rhs:
            sys.exit(1)


class SignatureRSA:
    def __init__(self, message):
        self.p = part_1.gen_p()
        self.q = part_1.gen_p()
        self.message = SHA256.new(message).digest()  # return

        self.n = self.p * self.q  # public
        self.f = (self.p - 1) * (self.q - 1)
        self.d = gen_coprime_integer_in_range(self.f, 1, self.f - 1)  # public
        self.c = modulo_inversion(self.d, self.f)  # secret

        self.s = 0  # return

    def encode(self):
        hash_f = int.from_bytes(self.message, 'big') % self.n
        self.s = part_1.fast_modulo_exponentiation(hash_f, self.c, self.n)

    def decode(self):
        hash_f = int.from_bytes(self.message, 'big') % self.n
        w = part_1.fast_modulo_exponentiation(self.s, self.d, self.n)

        print(hash_f)
        print(w)