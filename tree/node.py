class Node:
    def __init__(self, data, children = []):
        self.data = data
        self.children = children

    def __str__(self, level=0):
        strng = "  " * level + str(self.data) + "\n"

        for child in self.children:
            strng += child.__str__(level + 1)

        return strng

    def add_child(self, node):
        self.children.append(node)
