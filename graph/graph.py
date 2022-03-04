class Graph:
    def __init__(self, gdict=None):
        if not gdict:
            gdict = {}
        self.gdict = gdict
        
    def add_edge(self, vertex, edge):
        self.gdict[vertex].append(edge)

    def bfs(self, vertex):
        visited = [vertex]
        queue = [vertex]

        while queue:
            vertex = queue.pop(0)
            print(vertex)
            for adjacent in self.gdict[vertex]:
                if adjacent not in visited:
                    visited.append(adjacent)
                    queue.append(adjacent)

    def dfs(self, vertex):
        visited = [vertex]
        stack = [vertex]

        while stack:
            current_vertex = stack.pop()
            print(current_vertex)
            for adjacent in self.gdict[current_vertex]:
                if adjacent not in visited:
                    visited.append(adjacent)
                    stack.append(adjacent)

if __name__ == "__main__":
    dic = {
        "a": ["b", "c"],
        "b": ["b", "d", "e"],
        "c": ["a", "e"],
        "d": ["b", "e", "f"],
        "e": ["d", "f", "c"],
        "f": ["d", "e"]
    }

    g = Graph(dic)

    g.bfs("a")
    print("--------------------------")
    g.bfs("c")
    print("--------------------------")
    g.dfs("a")
    print("--------------------------")
    print("--------------------------")
