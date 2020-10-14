#!/usr/bin/python3

import random

import part_1


def gen_c(p):
    a = part_1.gen_p()
    while part_1.gcd(a, p - 1)[0] != 1:
        a = part_1.gen_p()
    return a


def shamir_protocol(file_path):
    # if not (isPrime(p) and (p > 255)): sys.exit('ERROR. [P] must be prime number or p <= 255.')

    with open(file_path, 'rb') as file:
        message = file.read()
    file.close()

    p = part_1.gen_p()

    c_a = gen_c(p)
    d_a = part_1.gcd(c_a, p - 1)[1]
    c_b = gen_c(p)
    d_b = part_1.gcd(c_b, p - 1)[1]

    if int.from_bytes(message, 'big') >= p:
        x1 = [0] * message.__len__()
        x2 = [0] * message.__len__()
        x3 = [0] * message.__len__()
        x4 = [0] * message.__len__()
        for i in range(0, message.__len__()):
            x1[i] = part_1.fast_modulo_exponentiation(message[i], c_a, p)
            x2[i] = part_1.fast_modulo_exponentiation(x1[i], c_b, p)
            x3[i] = part_1.fast_modulo_exponentiation(x2[i], d_a, p)
            x4[i] = part_1.fast_modulo_exponentiation(x3[i], d_b, p)
        output = bytearray(x4)
        with open("shamir_protocol_output.gif", 'wb') as file:
            file.write(output)
        for i in range(0, message.__len__()):
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
        x1 = part_1.fast_modulo_exponentiation(int.from_bytes(message, 'big'), c_a, p)
        x2 = part_1.fast_modulo_exponentiation(x1, c_b, p)
        x3 = part_1.fast_modulo_exponentiation(x2, d_a, p)
        x4 = part_1.fast_modulo_exponentiation(x3, d_b, p)

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

    # c_a = random.randint(1, p - 1)
    c_b = random.randint(1, p - 1)
    # d_a = part_1.fast_modulo_exponentiation(g, c_a, p)
    d_b = part_1.fast_modulo_exponentiation(g, c_b, p)

    if int.from_bytes(message, 'big') >= p:
        k = [0] * message.__len__()
        r = [0] * message.__len__()
        e = [0] * message.__len__()
        tmp = [0] * message.__len__()

        for i in range(0, message.__len__()):
            k[i] = random.randint(1, p - 2)
            r[i] = part_1.fast_modulo_exponentiation(g, k[i], p)
            e[i] = message[i] * part_1.fast_modulo_exponentiation(d_b, k[i], p)
            tmp[i] = e[i] * part_1.fast_modulo_exponentiation(r[i], p - 1 - c_b, p)

        result = bytearray(tmp)

        with open('elgamal_encryption_output.gif', 'wb') as file:
            file.write(result)

        for i in range(0, message.__len__()):
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
        r = part_1.fast_modulo_exponentiation(g, k, p)
        e = message * part_1.fast_modulo_exponentiation(d_b, k, p) % p
        mx = e * part_1.fast_modulo_exponentiation(r, p - 1 - c_b, p) % p
    if message == mx:
        print(message, ' == ', mx)
        print("Successful!")
        return True
    print(message, ' != ', mx)
    print("Error!")
    return False


class VernamEncryption:
    def __init__(self, file_path):
        with open(file_path, 'rb') as file:
            self.message = file.read()
        file.close()

        self.k = []
        for i in range(0, self.message.__len__()):
            self.k.append(random.randint(0, 255))

        self.tmp = [0] * self.message.__len__()
        self.decrypted_message = [0] * self.message.__len__()

    def encrypt(self):
        for i in range(0, self.message.__len__()):
            print(i)
            self.tmp[i] = self.message[i] ^ self.k[i]
        return self.tmp

    def decrypt(self):
        for i in range(0, self.message.__len__()):
            self.decrypted_message[i] = self.tmp[i] ^ self.k[i]
        return self.decrypted_message

    def compare(self):
        for i in range(0, self.message.__len__()):
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
    def __init__(self, file_path):
        with open(file_path, 'rb') as file:
            self.message = file.read()
        file.close()

        self.p, self.q = part_1.gen_p(), part_1.gen_p()

        self.n = self.p * self.q
        self.f = (self.p - 1) * (self.q - 1)
        self.d = part_1.gen_g(self.f)
        self.c = part_1.gcd(self.d, self.f)[1]

    def encrypt(self):
        result = [0] * self.message.__len__()
        for i in range(0, self.message.__len__()):
            result[i] = part_1.fast_modulo_exponentiation(self.message[i], self.d, self.n)
        return result

    def decrypt(self, message):
        result = [0] * message.__len__()
        for i in range(0, message.__len__()):
            result[i] = part_1.fast_modulo_exponentiation(message[i], self.c, self.n)
        return result

    @staticmethod
    def compare(lhs, rhs):
        for i in range(0, rhs.__len__()):
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
    print(part_1.gcd(19, 22))
    # print(shamir_protocol('file_path'))


if __name__ == "__main__":
    main()
