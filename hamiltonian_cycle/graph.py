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