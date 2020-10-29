import sys
import random
from Crypto.Hash import SHA256
from Crypto.Util import _number_new
from Crypto.Util import number

import part_1
from part_1 import fast_modulo_exponentiation as fme


def gen_g(p):
    if not part_1.is_prime(p):
        print('GEN_G: \'p\' is not prime !')

    g = random.randint(1, p - 1)

    while fme(g, (p - 1) / 2, p) == 1:
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
        self.open_key = fme(self.g, self.x, self.p)
        self.k = gen_coprime_integer_in_range(self.p - 1, 1, self.p - 1)
        self.r = fme(self.g, self.k, self.p)  # return

        self.u = 0
        self.s = 0  # return

    def encode(self):
        hash_f = int.from_bytes(self.message, 'big') % self.p
        self.u = (hash_f - self.x * self.r) % (self.p - 1)
        print(self.u)
        self.s = modulo_inversion(self.k, (self.p - 1)) * self.u % (self.p - 1)

    def decode(self):
        hash_f = int.from_bytes(self.message, 'big') % self.p
        lhs = (fme(self.open_key, self.r, self.p) * fme(self.r, self.s, self.p)) % self.p
        rhs = fme(self.g, hash_f, self.p)

        if lhs != rhs:
            sys.exit(1)


class SignatureRSA:
    def __init__(self, message):
        self.p = part_1.gen_p()
        self.q = part_1.gen_p()
        self.message = SHA256.new(message).digest()

        self.n = self.p * self.q  # public
        self.f = (self.p - 1) * (self.q - 1)
        self.d = gen_coprime_integer_in_range(self.f, 1, self.f - 1)  # public
        self.c = modulo_inversion(self.d, self.f)  # secret

        self.signature = 0

    def encode(self):
        hash_f = int.from_bytes(SHA256.new(self.message).digest(), 'big') % self.n
        self.signature = fme(hash_f, self.c, self.n)

    def decode(self):
        hash_f = int.from_bytes(SHA256.new(self.message).digest(), 'big') % self.n
        w = fme(self.signature, self.d, self.n)

        if hash_f != w:
            sys.exit(1)


class SignatureGOST:
    def __init__(self, message):
        self.message = SHA256.new(message).digest()  # return
        self.q = number.getPrime(2)  # 11
        self.p = number.getPrime(10)  # 67

        b = 0
        while b == 0:
            try:
                b = _number_new.exact_div(self.p - 1, self.q)
            except ValueError:
                self.q = number.getPrime(7)
                self.p = number.getPrime(20)

        self.a = self.p - 1
        while fme(self.a, self.q, self.p) != 1 and self.a > 1:
            self.a -= 1

        self.r = 0  # return
        self.s = 0  # return
        self.y = 0

        print('(' + str(self.p == b * self.q + 1) + ') p = bq + 1')
        print('(' + str(fme(self.a, self.q, self.p) == 1) + ') a^q mod p = 1')

    def encode(self):
        x = random.randint(1, self.q)  # 9 - secret key
        self.y = fme(self.a, x, self.p)  # open key

        h = int.from_bytes(self.message, 'big') % self.q

        k = self.q - 1  # 6

        while (self.r == 0 or self.s == 0) and k > 0:
            try:
                k -= 1
                self.r = fme(self.a, k, self.p) % self.q
                self.s = (k * h + x * self.r) % self.q
                print('r =', self.r, ' s =', self.s)
            except ValueError:
                print('Except. K =', k)
            continue

        if k == 0:
            raise Exception('Encode. Failed configuration.')

    def decode(self):
        h = int.from_bytes(self.message, 'big') % self.q

        if not (self.r < self.q or self.s < self.q):
            raise Exception('Decode. Failed configuration.')

        u_1 = self.s * modulo_inversion(h, self.q) % self.q
        u_2 = -self.r * modulo_inversion(h, self.q) % self.q

        v = ((self.a ** u_1 * self.y ** u_2) % self.p) % self.q

        print('(' + str(v == self.r) + ') v = r')


def main():
    with open('data/1.png', 'rb') as file:
        message = file.read()
    file.close()

    # instance = SignatureElGamal(message)
    # instance = SignatureRSA(message)
    # instance = SignatureGOST(message)

    # instance.encode()
    # instance.decode()


if __name__ == "__main__":
    main()
