import copy
import random

from hamiltonian_cycle.crypt import GraphRSA


class Swindler:
    def __init__(self, graph):
        self.graph = copy.deepcopy(graph)
        random.shuffle(self.graph.ham_cycle)

    def fraud(self):
        encrypted = GraphRSA(self.graph)
        try:
            encrypted.proof_cycle()
        except ValueError:
            print("""\nПроизошла попытка обмануть абонента.\nГамильтонов цикл не известен.""")
