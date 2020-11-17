from Functions.dimacs import *
from sys import argv
from Functions.GraphNode import *

def Stoera-Wagnera
if __name__ == "__main__":
    directory = argv
    directory = str(directory)
    directory = directory[2:-21] + "graphs/" + "conectivity2" + "/" + "path"
    (V,L) = loadWeightedGraph(directory)
    graf = Graph(V,L)
    print(graf)
    graf.mergeVertices(1,2)
    print(graf)
    graf.mergeVertices(2,3)
    print(graf)
    graf.mergeVertices(3,4)
    print(graf)
    graf.mergeVertices(4,5)
    print(graf)
    graf.mergeVertices(5,6)
    print(graf)
    graf.mergeVertices(6,6)
    print(graf)