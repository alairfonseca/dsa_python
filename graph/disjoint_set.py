class DisjointSet:
    def __init__(self, vertices):
        self.vertices = vertices
        self.rank = dict.fromkeys(vertices, 0)

        self.parent = {}
        for v in vertices:
            self.parent[v] = v

    def find(self, item):
        if self.parent[item] == item:
            return item
        else:
            return self.find(self.parent[item])

    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)

        if self.rank[xroot] < self.rank[yroot]:
            self.parent[xroot] = yroot
        elif self.rank[xroot] > self.rank[yroot]:
            self.parent[yroot] = xroot
        else:
            self.parent[yroot] = xroot
            self.rank[xroot] += 1

if __name__ == "__main__":
    v = ["a", "b", "c", "d", "e"]
    ds = DisjointSet(v)
    
    ds.union("a", "b")

    print(ds.find("b"))
