"""function we need to use to manipulate graph in this lab"""

"""function convert edge list to adjacency list """


def edge_list_to_adjacency_list(graph):
    # graph format V,L V-number of vertices L-list of edges
    adjacencyList = [[] for i in range(graph[0] + 1)]
    for i in graph[1]:
        adjacencyList[i[0]].append((i[1], i[2]))
        adjacencyList[i[1]].append((i[0], i[2]))
    return adjacencyList


"""" function uses dfs algorithm to finding patch from "start" to "end" with no using edges
with in weight less than limit, if find patch return true else return false """


def dfs_limited(graph, limit, start, end):
    # we give graph as adjacency list in format [[(V,W)] in n index we have list of edges where V is adjacent vertex
    # and W is weight of edge

    def DFS_Reku(g, l, s, e, colors):
        colors[s] = 'grey'
        if s == e:
            return True
        for i in g[s]:
            if colors[i[0]] == "white" and i[1] >= limit:
                return DFS_Reku(g, l, i[0], e, colors)
        colors[s] = "black"
    return DFS_Reku(graph, limit, start, end, ["white"] * len(graph)) or False
