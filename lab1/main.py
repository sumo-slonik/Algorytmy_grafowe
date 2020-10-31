""" main module of this laboratory"""

from FindUnionMethod import find_union_method
from dimacs import loadWeightedGraph
from Testing import testing
from BS_BFS_DFS import bs_dfs_method

from lab1.GraphFunctions import dfs_limited, edge_list_to_adjacency_list

if __name__ == "__main__":
    #print(dfs_limited(edge_list_to_adjacency_list(loadWeightedGraph("Graf/path10")), 11, 1, 2))
    print(bs_dfs_method(loadWeightedGraph("Graf/cloque5")))