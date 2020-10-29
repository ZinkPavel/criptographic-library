#!/usr/bin/python3

import random

import part_1
from part_1 import fast_modulo_exponentiation as fme


def gen_c(p):
    a = part_1.gen_p()
    while part_1.gcd(a, p - 1)[0] != 1:
        a = part_1.gen_p()
    return a


def shamir_protocol(file_path):
    with open(file_path, 'rb') as file:
        message = file.read()
    file.close()

    p = part_1.gen_p()

    c_a = gen_c(p)
    d_a = part_1.gcd(c_a, p - 1)[1]
    c_b = gen_c(p)
    d_b = part_1.gcd(c_b, p - 1)[1]

    if int.from_bytes(message, 'big') >= p:
        x1 = [0] * len(message)
        x2 = [0] * len(message)
        x3 = [0] * len(message)
        x4 = [0] * len(message)
        for i in range(0, len(message)):
            x1[i] = fme(message[i], c_a, p)
            x2[i] = fme(x1[i], c_b, p)
            x3[i] = fme(x2[i], d_a, p)
            x4[i] = fme(x3[i], d_b, p)
        output = bytearray(x4)
        with open("shamir_protocol_output.gif", 'wb') as file:
            file.write(output)
        for i in range(0, len(message)):
            if x4[i] == message[i]:
                print(x4[i], ' == ', message[i])
                continue
            else:
                print(x4[i], ' != ', message[i])
                print("Error!")
                return False
        print("Successful!")
        return True
    else:
        x1 = fme(int.from_bytes(message, 'big'), c_a, p)
        x2 = fme(x1, c_b, p)
        x3 = fme(x2, d_a, p)
        x4 = fme(x3, d_b, p)

        if not x4 == int.from_bytes(message, 'big'):
            print(x4, ' != ', message)
            print("Error!")
            return False
        print(x4, ' == ', message)
        print("Successful!")
        return True


def elgamal_encryption(file_path):
    with open(file_path, 'rb') as file:
        message = file.read()
    file.close()

    p = part_1.gen_p()
    g = part_1.gen_g(p)

    c_b = random.randint(1, p - 1)
    d_b = fme(g, c_b, p)

    if int.from_bytes(message, 'big') >= p:
        k = [0] * len(message)
        r = [0] * len(message)
        e = [0] * len(message)
        tmp = [0] * len(message)

        for i in range(0, len(message)):
            k[i] = random.randint(1, p - 2)
            r[i] = fme(g, k[i], p)
            e[i] = message[i] * fme(d_b, k[i], p)
            tmp[i] = e[i] * fme(r[i], p - 1 - c_b, p)

        result = bytearray(tmp)

        with open('elgamal_encryption_output.gif', 'wb') as file:
            file.write(result)

        for i in range(0, len(message)):
            if tmp[i] == message[i]:
                print(tmp[i], ' == ', message[i])
                continue
            else:
                print(tmp[i], ' != ', message[i])
                print("Error!")
                return False
        print('Successful')
        return True
    else:
        k = random.randint(1, p - 2)
        r = fme(g, k, p)
        e = message * fme(d_b, k, p) % p
        mx = e * fme(r, p - 1 - c_b, p) % p
    if message == mx:
        print(message, ' == ', mx)
        print("Successful!")
        return True
    print(message, ' != ', mx)
    print("Error!")
    return False


class VernamEncryption:
    def __init__(self, message):
        self.message = message
        self.k = []
        for i in range(0, len(self.message)):
            self.k.append(random.randint(0, 255))

        self.tmp = [0] * len(self.message)
        self.decrypted_message = [0] * len(self.message)

    def encrypt(self):
        for i in range(0, len(self.message)):
            print(i)
            self.tmp[i] = self.message[i] ^ self.k[i]
        return self.tmp

    def decrypt(self):
        for i in range(0, len(self.message)):
            self.decrypted_message[i] = self.tmp[i] ^ self.k[i]
        return self.decrypted_message

    def compare(self):
        for i in range(0, len(self.message)):
            if self.message[i] == self.decrypted_message[i]:
                print(self.decrypted_message[i], ' == ', self.message[i])
                continue
            else:
                print(self.decrypted_message[i], ' != ', self.message[i])
                print("Error!")
                return False
        print("Successful!")
        return True


class RSA:
    def __init__(self, message):
        self.message = message
        self.p, self.q = part_1.gen_p(), part_1.gen_p()

        self.n = self.p * self.q
        self.f = (self.p - 1) * (self.q - 1)
        self.d = part_1.gen_g(self.f)
        self.c = part_1.gcd(self.d, self.f)[1]

    def encrypt(self):
        result = [0] * len(self.message)
        for i in range(0, len(self.message)):
            result[i] = fme(self.message[i], self.d, self.n)
        return result

    def decrypt(self):
        result = [0] * len(self.message)
        for i in range(0, len(self.message)):
            result[i] = fme(self.message[i], self.c, self.n)
        return result

    @staticmethod
    def compare(lhs, rhs):
        for i in range(0, len(rhs)):
            if rhs[i] == lhs[i]:
                print(lhs[i], ' == ', rhs[i])
                continue
            else:
                print(lhs[i], ' != ', rhs[i])
                print("Error!")
                return False
        print("Successful!")
        return True


def main():
    with open('data/1.png', 'rb') as file:
        message = file.read()
    file.close()

    instance = RSA(message)


if __name__ == "__main__":
    main()
