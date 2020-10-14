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


def main():
    print(part_1.gcd(19, 22))
    # print(shamir_protocol('file_path'))


if __name__ == "__main__":
    main()