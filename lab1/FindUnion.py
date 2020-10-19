class union:
    # inicialize union class
    def __init__(self, vertices):
        # here we created array, in this array will be placed tuples
        # index of arr is representing number of verticle
        # first value in tuple is parent id secod value is rank in set
        self.vertices = [[i, 0] for i in range(0, vertices + 1)]

    # this function is looking for parent of verticle recurrently
    # and is making patch to parent shorter
    def find_set(self, x):
        if self.vertices[x][0] != x:
            self.vertices[x][0] = self.find_set(self.vertices[x][0])
        return self.vertices[x][0]

    # this function is mearging two sets in one by hieght od rank
    def make_union(self, x, y):
        x = self.find_set(x)
        y = self.find_set(y)
        if self.vertices[x][1] > self.vertices[y][1]:
            self.vertices[y] = [x, self.vertices[y][1]]
        else:
            self.vertices[x] = [y, self.vertices[x][1]]
            # if to sets are of the same rank we increment on of them before merge
            if self.vertices[x][1] == self.vertices[y][1]:
                self.vertices[y] = [y, self.vertices[y][1] + 1]

    # format to print function
    def __str__(self):
        return str(self.vertices)


if __name__ == "__main__":
    zbior = union(10)
    print("    ", end="")
    for i in range(0, 11):
        print("%-8d" % i, end="")
    print()
    print(zbior)
    zbior.make_union(5, 6)
    zbior.make_union(4, 6)
    zbior.make_union(3, 6)
    print(zbior)
