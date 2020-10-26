import random
import numpy as np

import part_1
from part_1 import fast_modulo_exponentiation as fme


class GraphRSA:
    def __init__(self, graph):
        self.graph = graph
        self.coded = np.zeros((8, 8))
        self.encrypted = np.zeros((8, 8))  # return

        self.p, self.q = part_1.gen_p(), part_1.gen_p()

        self.n = self.p * self.q
        self.f = (self.p - 1) * (self.q - 1)
        self.d = part_1.gen_g(self.f)
        self.c = part_1.gcd(self.d, self.f)[1]

    def encrypt(self):
        for i in range(0, len(self.graph.graph_h)):
            for j in range(0, len(self.graph.graph_h[i])):
                self.coded[i][j] += self.graph.graph_h[i][j] + random.randint(1, self.graph.n) * 10
                self.encrypted[i][j] += fme(self.coded[i][j], 3, self.n)

