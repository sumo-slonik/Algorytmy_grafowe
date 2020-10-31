from dimacs import loadWeightedGraph
from FindUnion import union
from sys import argv
from Testing import *
from GraphFunctions import edge_list_to_adjacency_list
'''This function make union class in size of vertex number 
    and then sorted edges in the descending desire, then we starting
    making union from the most weight edge and check is the start and and vertex in the
    same union. If yes we should return weight of last added vertex.
    '''


def find_union_method(name):
    Graph = loadWeightedGraph(name)
    Unia = union(Graph[0])
    Graph[1].sort(reverse=True, key=lambda x: x[2])
    result = None
    for i in Graph[1]:
        Unia.make_union(i[0], i[1])
        result = i[2]
        if Unia.find_set(1) == Unia.find_set(2):
            break
    return result
