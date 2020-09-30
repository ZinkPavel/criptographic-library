#!/usr/bin/python3

import sys
import math
import random

def isPrime(n):
    if (n <= 2): return False
    for num in range(2, math.floor(math.sqrt(n))):
        if (n % num == 0): return False
    return True

def fastModuloExponentiation(a, x, p):
    if x < 1 or x >= p: sys.exit('ERROR. [X] Must be from range (1, 2, ... , p-1)')
    
    result = 1
    t = math.floor(math.log2(x))
    tmp = a
    for num in range(t + 1):
        if num > 0: tmp *= tmp % p

        if (x % 2) == 1:
            result *= tmp
        x = x // 2

    return result % p 

def genEuclideanAlgo(a, b):
    if b > a: a, b = b, a
    
    U, V = [a, 1, 0], [b, 0, 1]

    while (V[0] != 0):
        tmp = U[0] // V[0]
        tmpList = U[0] % V[0], U[1] - tmp * V[1], U[2] - tmp * V[2]
        U, V = V, tmpList
    return U