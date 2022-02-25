from cqueue import CQueue

class LLTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return self.data

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

def levelorder_traversal(node):
    if not node:
        return
    
    q = CQueue()
    q.enqueue(node)

    while not q.is_empty():
        root = q.dequeue()
        print(root)
        if root._value._value.left is not None:
            q.enqueue(root._value._value.left)
        if root._value._value.right is not None:
            q.enqueue(root._value._value.right)

def search_binary_tree(node, target):
    if not node:
        return

    q = CQueue()
    q.enqueue(node)
    
    while not q.is_empty():
        root = q.dequeue()
        
        if root._value._value.data == target:
            return root._value._value.data

        if root._value._value.left is not None:
            q.enqueue(root._value._value.left)
        if root._value._value.right is not None:
            q.enqueue(root._value._value.right)

    return "Target not found"

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
    print("--------------")
    levelorder_traversal(t)

    print("--------------")
    print(search_binary_tree(t, "tea"))
    print(search_binary_tree(t, "coffe"))
    print(search_binary_tree(t, "coffee"))
