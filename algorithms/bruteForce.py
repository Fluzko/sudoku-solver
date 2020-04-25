import sys
import copy
import numpy as np


class BruteForce:
    def __init__(self, sudoku):
        self.board = sudoku
        self.max_solution = 0
        sys.setrecursionlimit(999999999)

    def solve(self):
        self.__solve__()
        return self.board

    def __solve__(self):
        solution = self.__initial_solution__()
        self.max_solution = solution * 9
        while solution:
            if self.__valid_solution__(solution):
                self.board = self.__apply_solution(solution)
                return
            solution = self.__next_solution__(solution)

        print('No se encontro solucion posible')
        sys.exit()

    def __all_solutions__(self):
        solutions = [self.__initial_solution__()]
        while self.__next_solution__(solutions[-1]):
            new_sol = self.__next_solution__(solutions[-1])
            solutions.append(new_sol)

        return solutions

    def __next_solution__(self, solution):
        # sum without 0's, for eg: 199 + 1 = 211 (real:200)
        solution += 1
        solution = int(str(solution).replace('0', '1'))
        if solution > self.max_solution:
            return None

        return solution

    def __valid_solution__(self, solution):
        applied_solution = self.__apply_solution(solution)
        for i in range(len(applied_solution)):
            for j in range(len(applied_solution[0])):
                if not self.__is_valid__(applied_solution[i][j], (i, j)):
                    return False
        return True

    def __initial_solution__(self):
        ceros = 0
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j] == 0:
                    ceros += 1
        return int('1' * ceros)

    def __apply_solution(self, solution):
        applied_solution = copy.deepcopy(self.board)
        str_solution = str(solution)
        num = 0
        for i in range(len(applied_solution)):
            for j in range(len(applied_solution[0])):
                if applied_solution[i][j] == 0:
                    applied_solution[i][j] = int(str_solution[num])
                    num += 1
        return applied_solution

    def __is_valid__(self, num, pos):
        # Check at the row
        for i in range(len(self.board[0])):
            if self.board[pos[0]][i] == num and pos[1] != i:
                return False

        # Check at the col
        for i in range(len(self.board)):
            if self.board[i][pos[1]] == num and pos[0] != i:
                return False

        # Check at the square
        sq_x = pos[1] // 3
        sq_y = pos[0] // 3

        for i in range(sq_y * 3, sq_y * 3 + 3):
            for j in range(sq_x * 3, sq_x * 3 + 3):
                if self.board[i][j] == num and (i, j) != pos:
                    return False

        # If passes all the validations, its valid
        return True
