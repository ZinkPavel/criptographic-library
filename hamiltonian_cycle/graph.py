import numpy as np
import random


class Graph:
    def __init__(self, file_path=''):
        self.n = 0
        self.m = 0
        self.cycle = [int]
        self.data = []
        self.graph_g = np.matrix
        self.graph_h = np.matrix
        self.file_path = file_path
        self.new_indices = []

        if not self.file_path == '':
            self.read_data()

    def read_data(self):
        if self.file_path == '':
            raise FileNotFoundError('File path = \"' + self.file_path + '\" not found')

        file = open(self.file_path)
        file = file.read().splitlines()

        self.n = int(file[0].split(' ')[0])
        self.m = int(file[0].split(' ')[1])
        self.cycle = file[-1].split(' ')
        self.graph_g = np.zeros((self.n, self.n))

        self.data = [line.split(' ') for line in file[1: -1]]
        self.data = [list(map(lambda elem: int(elem) - 1, elem)) for elem in self.data]

        for elem in self.data:
            self.graph_g[elem[0]][elem[1]] = 1
            self.graph_g[elem[1]][elem[0]] = 1

    def make_isomorphism_graph(self):
        tmp = [i for i in range(0, 8)]
        random.shuffle(tmp)
        self.new_indices = [tmp.index(i) for i in range(0, 8)]

        self.graph_h = np.zeros((8, 8))
        for elem in self.data:
            self.graph_h[self.new_indices[elem[0]]][self.new_indices[elem[1]]] = 1
            self.graph_h[self.new_indices[elem[1]]][self.new_indices[elem[0]]] = 1
