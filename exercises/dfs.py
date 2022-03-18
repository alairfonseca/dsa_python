class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Given a binary tree and a number ‘S’, find if the tree has a path from root-to-leaf such that the sum of all the node values of that path equals ‘S’.
def has_path(root, path_sum):
    if not root:
        return False

    if root.val == path_sum and not root.left and not root.right:
        return True
    
    return has_path(root.left, path_sum - root.val) or has_path(root.right, path_sum - root.val)


# Given a binary tree and a number ‘S’, find all paths from root-to-leaf such that the sum of all the node values of each path equals ‘S’.
def find_paths(root, path_sum):
    result = []

    find_paths_rec(root, path_sum, [], result)

    return result

def find_paths_rec(current_node, required_sum, current_path, paths):
    if not current_node:
        return

    current_path.append(current_node.val)

    if current_node.val == required_sum and not current_node.left and not current_node.right:
        paths.append(list(current_path))
    else:
        find_paths_rec(current_node.left, required_sum - current_node.val, current_path, paths)
        
        find_paths_rec(current_node.right, required_sum - current_node.val, current_path, paths)

    current_path.pop()

def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree has path: " + str(has_path(root, 23)))
    print("Tree has path: " + str(has_path(root, 16)))

    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    sum = 23
    print("Tree paths with sum " + str(sum) + ": " + str(find_paths(root, sum)))


main()

