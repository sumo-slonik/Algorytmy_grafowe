class Node:
    def __init__(self, id):
        self.edges = {}
        self.active = True
        self.mergeWith = [id]
        self.id = id

    def addEdge(self, to, weight):
        self.edges[to] = self.edges.get(to, 0) + weight

    def delEdge(self, to):
        del self.edges[to]

    def __str__(self):
        result = ""
        for i in self.edges:
            result += str((i, self.edges[i])) + ","
        result = result[:-1]
        return result


class Graph:
    def __init__(self, V, L, directed=False):
        self.vertices = [Node(i) for i in range(0, V + 1)]
        if directed:
            for (x, y, c) in L:
                self.vertices[x].addEdge(y, c)
        else:
            for (x, y, c) in L:
                self.vertices[x].addEdge(y, c)
                self.vertices[y].addEdge(x, c)

    def __str__(self):
        maks = max([len(str(i.mergeWith)) for i in self.vertices])
        result = "{0:{maks}}   {1:^7}  Edges:(to,weight)\n".format("V","Status",maks = maks)
        for j, i in enumerate(self.vertices):
            if j != 0:
                actual = "{0:{maks}}"+"  "+"{1:^7}"+"   " + str(i) + "\n"
                actual = actual.format(str(i.mergeWith),str(i.active),maks=maks)
                result+=actual
        return result

    # del all edges from x and copy this edges to y
    def mergeVertices(self, x, y):
        toDel = self.vertices[x]
        toAdd = self.vertices[y]
        if toDel.id != toAdd.id:
            # need to use key list because we will be deleting values
            if self.vertices[x].active:
                for i in list(toDel.edges.keys()):
                    if i != toAdd.id:
                        toAdd.addEdge(i, toDel.edges[i])
                        toDel.active = False
                    toDel.delEdge(i)
                for j in toDel.mergeWith:
                    toAdd.mergeWith.append(j)

if __name__ == "__main__":
    k = "kuba"
    k += str([1, 2, 3, 4])
    print(k)
