from _collections import deque
from Functions.dimacs import loadDirectedWeightedGraph

class Graph:
    def __init__(self, V, L, t="adj",directed = True):
        self.V = V
        self.type = t
        if t == "adj":
            self.E = [[None] for _ in range(self.V + 1)]
        elif t == "matrix":
            self.E = [[0 for _ in range(V + 1)] for _ in range(V + 1)]
            for i in L:
                if directed:
                    self.E[i[0]][i[1]] = i[2]
                else:
                    self.E[i[0]][i[1]] = i[2]
                    self.E[i[1]][i[0]] = i[2]
        else:
            self.E = []

    def bfs(self, start, stop):
        def bfs_matrix(start, stop):
            que = [start]
            parents = [None for _ in range(self.V + 1)]
            visited = [False for _ in range(self.V + 1)]
            while que:
                actual = que.pop()
                visited[actual] = True
                for v, weight in enumerate(self.E[actual]):
                    if visited[v] is False and weight > 0:
                        parents[v] = actual
                        que.append(v)
            return visited[stop],parents
        return bfs_matrix(start, stop)

if __name__ == "__main__":
    graf = loadDirectedWeightedGraph("D:/Algorytmy_grafowe/graphs/flow/simple")
    graf = Graph(*graf, "matrix")
    for i in graf.E:
         print(i)
    graf.bfs(1,3)
