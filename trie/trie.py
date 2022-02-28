from node import Node

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, strng):
        current = self.root

        for ch in strng:
            node = current.children.get(ch)

            if not node:
                node = Node()
                current.children.update({ch: node})
            current = node
        current.eos = True

    def search(self, target):
        current = self.root

        for ch in target:
            node = current.children.get(ch)

            if not node:
                return False

            current = node
        if current.eos:
            return True
        return False

    def __str__(self):
        return self.rec_str(self.root)

    def rec_str(self, node, prefix="", result=[]):
        if node.eos and len(node.children.keys()):
            result.append(prefix)

        if not len(node.children.keys()):
            result.append(prefix)
            return prefix

        for k in node.children:
            self.rec_str(node.children[k], (prefix + k))

        return ", ".join(result)

if __name__ == "__main__":
    t = Trie()

    t.insert("app")
    t.insert("appl")
    t.insert("apple")
    t.insert("ago")
    t.insert("agu")
    t.insert("car")
    t.insert("cargo")
    t.insert("aprove")
    t.insert("approve")

    print(t)
    print("----------------------")
    print(t.search("app"), end=" - ")
    print(t.search("app1"), end=" - ")
    print(t.search("apple"))
    print("----------------------")
    print("----------------------")
    print("----------------------")
    print("----------------------")
    print("----------------------")
