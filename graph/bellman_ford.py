class Graph:
    def __init__(self, vertices):
        self.v = vertices
        self.graph = []
        self.nodes = []

    def add_edge(self, s, d, w):
        self.graph.append([s, d, w])


    def add_node(self, value):
        self.nodes.append(value)

    def print_solution(self, dist):
        for k, v in dist.items():
            print(" ", k, ":  ", v)

    def bellman_ford(self, src):
        dist = { i: float("Inf") for i in self.nodes }
        dist[src] = 0
        
        for _ in range(self.v - 1):
            for s, d, w in self.graph:
                if dist[s] != float("Inf") and dist[s] + w < dist[d]:
                    dist[d] = dist[s] + w

        for s, d, w in self.graph:
            if dist[s] != float("Inf") and dist[s] + w < dist[d]:
                print("negative cycle")
                return

        self.print_solution(dist)


if __name__ == "__main__":
    g = Graph(5)

    g.add_node("a")
    g.add_node("b")
    g.add_node("c")
    g.add_node("d")
    g.add_node("e")

    g.add_edge("a", "c", 6)
    g.add_edge("a", "d", 6)
    g.add_edge("b", "a", 3)
    g.add_edge("c", "d", 1)
    g.add_edge("d", "c", 2)
    g.add_edge("d", "b", 1)
    g.add_edge("e", "b", 4)
    g.add_edge("e", "d", 2)

    g.bellman_ford("e")
