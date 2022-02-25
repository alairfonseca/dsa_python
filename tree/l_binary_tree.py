# Binary tree based on python list
class LBinaryTree:
    def __init__(self, size):
        self.list = [None] * size
        self.last_used_index = 0
        self.max_size = size

    def insert(self, value):
        if self.last_used_index + 1 == self.max_size:
            raise Exception("Tree is full")
        
        self.list[self.last_used_index + 1] = value
        self.last_used_index += 1

    def search(self, value):
        for i in self.list:
            if i == value:
                return value
        return "Node not found"

    def preorder_traversal(self, index):
        if index > self.last_used_index:
            return
        
        print(self.list[index])
        
        self.preorder_traversal(index * 2)
        self.preorder_traversal(index * 2 + 1)

    def inorder_traversal(self, index):
        if index > self.last_used_index:
            return
        
        self.inorder_traversal(index * 2)
        print(self.list[index])
        self.inorder_traversal(index * 2 + 1)
    
    def postorder_traversal(self, index):
        if index > self.last_used_index:
            return
        
        self.postorder_traversal(index * 2)
        self.postorder_traversal(index * 2 + 1)
        print(self.list[index])

if __name__ == "__main__":
    t = LBinaryTree(10)
    
    t.insert("drinks")
    t.insert("hot")
    t.insert("cold")

    t.insert("tea")
    t.insert("coffee")

    t.insert("cola")
    t.insert("soda")


    print("---------------------")
    t.preorder_traversal(1)
    print("---------------------")
    t.inorder_traversal(1)
    print("---------------------")
    t.postorder_traversal(1)

    print("---------------------")
    print(t.search("tea"))
    print(t.search("col"))
    print(t.search("cola"))
