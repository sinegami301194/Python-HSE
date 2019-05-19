from sys import stdin


class Matrix:
    def __init__(self, matrix=[[]]):
        self.matrix = matrix.copy()

    def __str__(self):
        return '\n'.join([''.join(['%d\t' % i for i in row])
                          for row in matrix])

    def size(self):
        rows = len(self.matrix)
        cols = 0
        for row in self.matrix:
            if len(row) > cols:
                cols = len(row)
        return (rows, cols)
exec(stdin.read())
