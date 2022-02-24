class LLTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def preorder_traversal(node):
    if not node:
        return
    print(node.data)
    preorder_traversal(node.left)
    preorder_traversal(node.right)

def inorder_traversal(node):
    if not node:
        return
    inorder_traversal(node.left)
    print(node.data)
    inorder_traversal(node.right)

def postorder_traversal(node):
    if not node:
        return
    postorder_traversal(node.left)
    postorder_traversal(node.right)
    print(node.data)

if __name__ == "__main__":
    t = LLTree("drinks")
    
    t.left = LLTree("cold")
    t.left.left = LLTree("fanta")
    t.left.right = LLTree("soda")
    t.right = LLTree("hot")
    t.right.left = LLTree("coffee")
    t.right.right = LLTree("tea")

    preorder_traversal(t)
    print("--------------")
    inorder_traversal(t)
    print("--------------")
    postorder_traversal(t)
