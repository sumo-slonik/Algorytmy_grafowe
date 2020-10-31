from lab2.FordFulkerson import *


def Connectivity(name):
    tmpGraph = loadDirectedWeightedGraph(name)
    tmpGraph = Graph(*tmpGraph, "matrix")
    for _ in tmpGraph.E:
        for index, edge in enumerate(_):
            if edge != 0:
                # print(_)
                # print(index)
                _[index] = 1
    return FordFulkerson(tmpGraph, 1, tmpGraph.V)
