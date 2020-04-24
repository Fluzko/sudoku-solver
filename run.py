from sudoku import sudoku as sk, algorithm as alg, graph as gp
from algorithms import backtrack
from graphs import console
import sys


def get_solver(string_solver):
    possible_solvers = [
        ('backtrack', backtrack.Backtrack)
    ]
    solver = None
    for s in possible_solvers:
        if string_solver == s[0]:
            solver = s[1]

    if not solver:
        print('Algoritmo invalido')
        sys.exit()

    return solver


def get_graph(string_graph):
    possible_graphs = [
        ('console', console.ConsoleGraph)
    ]
    graph = None
    for g in possible_graphs:
        if string_graph == g[0]:
            graph = g[1]

    if not graph:
        print('Graficador invalido')
        sys.exit()

    return graph


solver_class = get_solver(alg)
graph_class = get_graph(gp)

solver = solver_class(sk)
solver.solve()
graph_class(solver.board).graph()
