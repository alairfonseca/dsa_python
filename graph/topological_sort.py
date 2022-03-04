from collections import defaultdict

class Graph:
    def __init__(self, number_of_vertices):
        self.graph = defaultdict(list)
        self.number_of_vertices = number_of_vertices

    def add_edge(self, vertex, edge):
        self.graph[vertex].append(edge)

    def topological_sort_util(self, v, visited, stack):
        visited.append(v)
        
        for i in self.graph[v]:
            if i not in visited:
                self.topological_sort_util(i, visited, stack)

        stack.insert(0, v)

    def topological_sort(self):
        visited = []
        stack = []

        for k in list(self.graph):
            if k not in visited:
                self.topological_sort_util(k, visited, stack)

        print(stack)

if __name__ == "__main__":
    g = Graph(8)
    
    g.add_edge("a", "c")
    g.add_edge("c", "e")
    g.add_edge("e", "h")
    g.add_edge("e", "f")
    g.add_edge("f", "g")
    g.add_edge("b", "d")
    g.add_edge("b", "c")
    g.add_edge("d", "c")
    
    g.topological_sort()
