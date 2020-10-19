"""function we need to use to manipulate graph in this lab"""

"""function convert edge list to adjacency list """


def edge_list_to_adjacency_list(graph):
    # graph format V,L V-number of vertices L-list of edges
    adjacencyList = [[] for i in range(graph[0] + 1)]
    for i in graph[1]:
        adjacencyList[i[0]].append(i[2])
        adjacencyList[i[1]].append(i[2])
    return adjacencyList

