from cqueue import CQueue

class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, value):
    if root.data == None:
        root.data = value
    elif value <= root.data:
        if root.left == None:
            root.left = BSTNode(value)
        else:
            insert(root.left, value)
    else:
        if root.right == None:
            root.right = BSTNode(value)
        else:
            insert(root.right, value)

def preorder_traversal(root):
    if not root:
        return
    
    print(root.data)
    preorder_traversal(root.left)
    preorder_traversal(root.right)

def inorder_traversal(root):
    if not root:
        return
    
    inorder_traversal(root.left)
    print(root.data)
    inorder_traversal(root.right)

def postorder_traversal(root):
    if not root:
        return
    
    postorder_traversal(root.left)
    postorder_traversal(root.right)
    print(root.data)

def levelorder_traversal(root):
    if not root:
        return
    q = CQueue()
    q.enqueue(root)

    while not q.is_empty():
        root = q.dequeue()
        print(root._value._value.data)

        if root._value._value.left is not None:
            q.enqueue(root._value._value.left)
        if root._value._value.right is not None:
            q.enqueue(root._value._value.right)

def search(root, target):
    if root.data == target:
        return root.data

    if target < root.data:
        if not root.left:
            return "Not found"
        if root.left.data == target:
            return root.left.data
        else:
            return search(root.left, target)
    else:
        if not root.right:
            return "Not found"
        if root.right.data == target:
            return root.right.data
        else:
            return search(root.right, target)


if __name__ == "__main__":
    bst = BSTNode(None)

    insert(bst, 70)
    insert(bst, 50)
    insert(bst, 90)
    insert(bst, 40)
    insert(bst, 60)
    insert(bst, 65)
    insert(bst, 50)
    insert(bst, 45)
    insert(bst, 43)

    preorder_traversal(bst)
    print("--------------------")
    inorder_traversal(bst)
    print("--------------------")
    postorder_traversal(bst)
    print("--------------------")
    levelorder_traversal(bst)
    print("--------------------")
    print(search(bst, 65))
    print(search(bst, 45))
    print(search(bst, 43))
    print(search(bst, 71))
    print("--------------------")
    print("--------------------")
    print("--------------------")
