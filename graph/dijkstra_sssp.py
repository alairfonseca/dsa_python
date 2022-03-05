from collections import defaultdict

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, a, b, distance):
        self.edges[a].append(b)
        self.distances[(a, b)] = distance

def dijkstra(graph, initial):
    visited = { initial: 0 }
    path = defaultdict(list)

    nodes = set(graph.nodes)

    while nodes:
        min_node = None

        for node in nodes:
            if node in visited:
                if not min_node:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node
        if not min_node:
            break

        nodes.remove(min_node)
        current_weight = visited[min_node]

        for edge in graph.edges[min_node]:
            weight = current_weight + graph.distances[(min_node, edge)]

            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge].append(min_node)

    return visited, path

if __name__ == "__main__":
    g = Graph()

    g.add_node("a")
    g.add_node("b")
    g.add_node("c")
    g.add_node("d")
    g.add_node("e")
    g.add_node("f")
    g.add_node("g")

    g.add_edge("a", "b", 2)
    g.add_edge("a", "c", 5)
    g.add_edge("b", "c", 6)
    g.add_edge("b", "d", 1)
    g.add_edge("b", "e", 3)
    g.add_edge("c", "f", 8)
    g.add_edge("d", "e", 4)
    g.add_edge("e", "g", 9)
    g.add_edge("f", "g", 7)

    print(dijkstra(g, "a"))
