#!/usr/bin/python3

import sys
import math
import random


def miller_rabin_test(n, k):
    if n == 2 or n == 3:
        return True

    if n < 2 or n % 2 == 0:
        return False

    t, s = n - 1, 0

    while t % 2 == 0:
        t, s = t / 2, s + 1

    for i in range(0, k):
        a = random.randint(2, n - 2)
        x = fast_modulo_exponentiation(a, int(t), int(n))

        if x == 1 or x == n - 1:
            continue

        for r in range(1, s):
            x = fast_modulo_exponentiation(x, 2, n)

            if x == 1:
                return False

            if x == n - 1:
                break

        if x != n - 1:
            return False

    return True


def gen_p():
    p = random.randint(10 ** 6, 10 ** 9)

    while not (miller_rabin_test(p, int(math.log2(p))) and miller_rabin_test(p * 2 + 1, int(math.log2(p * 2 + 1)))):
        p = random.randint(10 ** 6, 10 ** 9)

    return 2 * p + 1


def gen_g(p):
    while True:
        g = random.randint(2, 100)
        # g = random.randint(1, p - 1)
        if fast_modulo_exponentiation(g, int((p - 1) / 2), p) != 1 and is_prime(g):
            return g


def is_prime(n):
    if n <= 2:
        return False

    for num in range(2, math.floor(math.sqrt(n))):
        if n % num == 0:
            return False

    return True


def fast_modulo_exponentiation(a, x, p):
    result, tmp = 1, a
    t = math.floor(math.log2(x))

    for num in range(t + 1):
        if num > 0:
            tmp *= tmp % p

        if (x % 2) == 1:
            result *= tmp

        x = x // 2

    return result % p


def gcd(a, b):
    if b > a:
        a, b = b, a

    u, v = [a, 1, 0], [b, 0, 1]

    while v[0] != 0:
        tmp = u[0] // v[0]
        tmp_list = u[0] % v[0], u[1] - tmp * v[1], u[2] - tmp * v[2]
        u, v = v, tmp_list
    return u


def diffie_hellman_protocol(p, g):
    if not is_prime(p):
        sys.exit('ERROR. [P] must be prime number.')

    q = (p - 1) / 2  # reverse

    if not is_prime(q):
        sys.exit('ERROR. [Q] must be prime number.')

    if 1 >= g >= p - 1:
        sys.exit('ERROR. [G] Must be (1 < g < p - 1)')

    if fast_modulo_exponentiation(g, q, p) == 1:
        sys.exit('ERROR. [G] Must be (g^q mod p != 1)')

    x_a, x_b = random.randint(1, 10), random.randint(1, 10)
    y_a, y_b = fast_modulo_exponentiation(g, x_a, p), fast_modulo_exponentiation(g, x_b, p)
    z_a, z_b = fast_modulo_exponentiation(y_b, x_a, p), fast_modulo_exponentiation(y_a, x_b, p)

    if z_a != z_b:
        sys.exit(1)

    return z_a


def first_entry(seq, x):
    index = 0

    for elem in seq:
        if elem == x:
            return index
        index += 1

    return -1


def baby_giant_step(a, p, y):
    # random generate m & k
    m, k = random.randint(1, 10) * math.floor(math.sqrt(p)) + 1, random.randint(1, 10) * math.floor(math.sqrt(p)) + 1
    # --------------

    result = [0, 0]
    giant_steps, baby_steps = [fast_modulo_exponentiation(a, m, p)], [y]

    for j in range(1, m):
        baby_steps.append((a * baby_steps[j - 1]) % p)  # in this case faster than call.fastModuloExponentiation()

    for i in range(1, k - 1):
        result[i] = first_entry(baby_steps, giant_steps[i - 1])

        if result[i] != -1:
            result[0] = i
            break

        giant_steps.append((giant_steps[i - 1] * giant_steps[i - 1]) % p)

    return result[0] * m - result[1]
