from Functions.Graph import *
from Functions.dimacs import *

'''
This is function to find max flow in directed weight graph using Ford–Fulkerson method.
Max flow is returned as result of function,if flow is not find is result is equal to 0
Uses matrix representation of graph
'''
def FordFulkerson(graf, source, slink):
    flow = 0
    # finding first patch between source and sink
    # in parents array in i index we have number of vertex from we come to i index in bfs
    # necessary_condition is true if we can find patch between source and sink
    necessary_condition, parents = graf.bfs(source, slink)
    while necessary_condition:
        patchFlow = float("inf")
        end = slink
        # finding value of flow in actual flow
        while end != source:
            patchFlow = min(patchFlow, graf.E[parents[end]][end])
            end = parents[end]
        flow += patchFlow
        end = slink
        # updating graph by actual patch flow
        while end != source:
            endParent = parents[end]
            graf.E[end][endParent] += patchFlow
            graf.E[endParent][end] -= patchFlow
            end = endParent
        # looking for new patch in graph
        necessary_condition, parents = graf.bfs(source, slink)
    return flow
'''
This function prepare Ford–Fulkerson function to be tested with testing function.
'''
def FordFulkersonWraper(name):
    tmpGraph = loadDirectedWeightedGraph(name)
    tmpGraph = Graph(*tmpGraph, "matrix")
    return FordFulkerson(tmpGraph, 1, tmpGraph.V)


