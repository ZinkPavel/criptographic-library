import numpy as np


class Matrix:
    def __init__(self, file_path=''):
        self.n = 0
        self.m = 0
        self.cycle = [int]
        self.data = np.matrix
        self.file_path = file_path

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
        self.data = np.zeros((self.n, self.n))

        matrix_data = [line.split(' ') for line in file[1: -1]]
        for elem in matrix_data:
            self.data[int(elem[0]) - 1][int(elem[1]) - 1] = 1
            self.data[int(elem[1]) - 1][int(elem[0]) - 1] = 1
