from dimacs import loadWeightedGraph
from GraphFunctions import dfs_limited, edge_list_to_adjacency_list


def bs_dfs_method(graph):
    weights = [i[2] for i in graph[1]]
    weights.sort()
    i = len(weights) - 1
    j = 0
    adjacency_list = edge_list_to_adjacency_list(graph)
    while True:
        limit = weights[(i + j) // 2]
        if abs(i - j) <= 1:
            break
        if dfs_limited(adjacency_list, limit, 1, 2):
            j, i = (i + j) // 2 + 1, i
        else:
            j, i = j, (i + j) // 2 - 1
    if dfs_limited(adjacency_list, weights[i], 1, 2):
        return weights[i]
    elif dfs_limited(adjacency_list, weights[j], 1, 2):
        return weights[j]
    else:
        return None
