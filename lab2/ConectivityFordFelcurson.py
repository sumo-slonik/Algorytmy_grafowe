from lab2.FordFulkerson import *
from copy import deepcopy
from lab2.FordFulkerson import *


def Connectivity(name):
    tmpGraph = loadWeightedGraph(name)
    tmpGraph = Graph(*tmpGraph, "matrix", False)
    for _ in tmpGraph.E:
        for index, edge in enumerate(_):
            if edge != 0:
                _[index] = 1
    minimum = float("inf")
    for v1 in range(1, tmpGraph.V):
        for v2 in range(v1 + 1, tmpGraph.V + 1):
            actual = FordFulkerson(deepcopy(tmpGraph), v1, v2)
            if actual < minimum:
                minimum = actual
    return minimum
