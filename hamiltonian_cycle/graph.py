import numpy as np
import random

from hamiltonian_cycle.cycle import HamiltonianCycle


class Graph:
    def __init__(self, file_path='', n=0, m=0, data=np.matrix):
        self.vertices, self.edges = n, m
        self.points = [int]
        self.data = data
        self.alt_indices = [int]
        self.ham_cycle = HamiltonianCycle

        if not file_path == '':
            self.read_graph(file_path)

    def read_graph(self, file_path):
        if file_path == '':
            raise FileNotFoundError('File path = \"' + file_path + '\" not found')

        file = open(file_path)
        file = file.read().splitlines()

        self.vertices = int(file[0].split(' ')[0])
        self.edges = int(file[0].split(' ')[1])

        if self.vertices >= 1001:
            raise ValueError('Error: non valid num vertices')

        if self.edges > self.vertices ** 2:
            raise ValueError('Error: non valid num edges')

        self.ham_cycle = list(map(lambda elem: int(elem) - 1, file[-1].split(' ')))

        self.points = list(map(lambda line: line.split(' '), file[1: -1]))
        self.points = [list(map(lambda elem: int(elem) - 1, pair)) for pair in self.points]

        self.data = np.zeros((self.vertices, self.vertices))
        for point in self.points:
            self.data[point[0]][point[1]] = 1
            self.data[point[1]][point[0]] = 1

    def make_isomorphism_graph(self):
        self.alt_indices = list(range(0, self.vertices))
        random.shuffle(self.alt_indices)

        new_graph = np.zeros((self.vertices, self.vertices))
        for elem in self.points:
            new_graph[self.alt_indices[elem[0]]][self.alt_indices[elem[1]]] = 1
            new_graph[self.alt_indices[elem[1]]][self.alt_indices[elem[0]]] = 1

        result = Graph()
        result.vertices, result.edges = self.vertices, self.edges
        result.data = new_graph
        # indices
        return result
