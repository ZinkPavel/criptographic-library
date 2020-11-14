import random
import numpy as np

import part_1
from part_1 import fast_modulo_exponentiation as fme


class GraphRSA:
    def __init__(self, graph):
        self.graph = graph
        self.coded = np.zeros((8, 8), dtype=int)
        self.encrypted = np.zeros((8, 8), dtype=int)  # return

        self.p, self.q = part_1.gen_p(), part_1.gen_p()

        self.n = self.p * self.q
        self.f = (self.p - 1) * (self.q - 1)
        self.d = part_1.gen_g(self.f)
        self.c = part_1.gcd(self.d, self.f)[1]

    def encrypt(self):
        for i in range(0, len(self.graph.isom_graph)):
            for j in range(0, len(self.graph.isom_graph[i])):
                self.coded[i][j] += self.graph.isom_graph[i][j] + random.randint(1, 10) * 10
                self.encrypted[i][j] += fme(self.coded[i][j], 3, self.n)

    def proof_isomorphism(self):
        for i in range(0, len(self.graph.isom_graph)):
            for j in range(0, len(self.graph.isom_graph[i])):
                tmp = fme(self.coded[i][j], 3, self.n)

                if not tmp == self.encrypted[i][j]:
                    raise ValueError('Error:' + str(tmp) + '!=' + str(self.encrypted[i][j]))

        result = np.zeros((8, 8))
        for i in range(0, len(self.graph.isom_graph)):
            for j in range(0, len(self.graph.isom_graph[i])):
                result[i][j] = self.coded[i][j] % 10

        for elem in self.graph.isom_graph:
            if not result[self.graph.alt_indices[elem[0]]][self.graph.alt_indices[elem[1]]] == self.graph.data[elem[0]][elem[1]]:
                raise ValueError('Error: proof isomorphism 1.1')
            if not result[self.graph.alt_indices[elem[1]]][self.graph.alt_indices[elem[0]]] == self.graph.data[elem[1]][elem[0]]:
                raise ValueError('Error: proof isomorphism 1.2')

    def proof_cycle(self):
        for elem in self.graph.data:
            actual = self.coded[self.graph.alt_indices[elem[0]]][self.graph.alt_indices[elem[1]]]
            expect = self.encrypted[self.graph.alt_indices[elem[0]]][self.graph.alt_indices[elem[1]]]

            if not fme(actual, 3, self.n) == expect:
                raise ValueError('Error: proof cycle 1.1')

        cycle = self.graph.ham_cycle

        for i in range(0, len(self.graph.ham_cycle) - 1):
            if not [cycle[i], cycle[i+1]] in self.graph.points:
                if not [cycle[i+1], cycle[i]] in self.graph.points:
                    raise ValueError('Error: proof cycle 1.2')
