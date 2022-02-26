from cqueue import CQueue

class AVLNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1
    
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

def get_height(root):
    if not root:
        return 0
    return root.height

def right_rotate(root):
    new_root = root.left
    root.left = root.left.right
    new_root.right = root

    root.height = max(get_height(root.left), get_height(root.right)) + 1
    new_root.height = max(get_height(new_root.left), get_height(new_root.right)) + 1

    return new_root

def left_rotate(root):
    new_root = root.right
    root.right = root.right.left
    new_root.left = root

    root.height = max(get_height(root.left), get_height(root.right)) + 1
    new_root.height = max(get_height(new_root.left), get_height(new_root.right)) + 1

    return new_root

def get_balance(root):
    if not root:
        return 0
    return get_height(root.left) - get_height(root.right)

def insert(root, value):
    if not root:
        return AVLNode(value)
    elif value < root.data:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)

    root.height = max(get_height(root.left), get_height(root.right)) + 1
    
    balance = get_balance(root)

    if balance > 1 and value < root.left.data:
        return right_rotate(root)
    if balance > 1 and value > root.left.data:
        root.left = left_rotate(root)
        return right_rotate(root)
    if balance < -1 and value > root.right.data:
        return left_rotate(root)
    if balance < -1 and value < root.right.data:
        root.right = right_rotate(root.right)
        return left_rotate(root)
    
    return root

def min_value(root):
    if root is None or root.left is None:
        return root
    return min_value(root.left)

def delete(root, target):
    if not root:
        return root
    elif target < root.data:
        root.left = delete(root.left, target)
    elif target > root.data:
        root.right = delete(root.right, target)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        temp = min_value(root.right)
        root.data = temp.data
        root.right = delete(root.right, temp.data)
    balance = get_balance(root)
    if balance > 1 and get_balance(root.left) >= 0:
        return right_rotate(root)
    if balance < -1 and get_balance(root.right) <= 0:
        return left_rotate(root)
    if balance > 1 and get_balance(root.left) < 0:
        root.left = left_rotate(root.left)
        return right_rotate(root)
    if balance < -1 and get_balance(root.right) > 0:
        root.right = right_rotate(root.right)
        return left_rotate(root)


if __name__ == "__main__":
    avl = AVLNode(5)
    avl = insert(avl, 10)
    avl = insert(avl, 15)
    avl = insert(avl, 20)
    
    #preorder_traversal(avl)
    #print("--------------------")
    #inorder_traversal(avl)
    #print("--------------------")
    #postorder_traversal(avl)
    print("--------------------")
    delete(avl, 15)
    levelorder_traversal(avl)
    print("--------------------")
    print("--------------------")
    print("--------------------")
