from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


# Given a binary tree, populate an array to represent its level-by-level traversal. You should populate the values of all nodes of each level from left to right in separate sub-arrays.
def traverse(root):
    result = []
    queue = [root]

    while queue:
        level_size = len(queue)
        current_level = []
        for _ in range(level_size):
            node = queue.pop(0)
            
            current_level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(current_level)

    return result

"""
Given a binary tree, populate an array to represent its level-by-level traversal in reverse order,
i.e., the lowest level comes first. You should populate the values of all nodes in each level from
left to right in separate sub-arrays.
"""
def traverse2(root):
    result = deque()
    queue = [root]
    
    while queue:
        level_size = len(queue)
        current_level = []

        for _ in range(level_size):
            node = queue.pop(0)
            current_level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.appendleft(current_level)

    return result

"""
Given a binary tree, populate an array to represent its zigzag level order traversal.
You should populate the values of all nodes of the first level from left to right, then
right to left for the next level and keep alternating in the same manner for the following levels.
"""
def zigzag(root):
    result = []
    zig = True
    queue = [root]
    
    while queue:
        level_size = len(queue)
        current_level = []

        for _ in range(level_size):
            node = queue.pop(0)

            if zig:
                current_level.append(node.val)
            else:
                current_level.insert(0, node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(current_level)
        zig = not zig

    return result


# Given a binary tree, populate an array to represent the averages of all of its levels.
def find_level_averages(root):
    result = []
    queue = [root]

    while queue:
        level_size = len(queue)
        level_sum = 0.0
        
        for _ in range(level_size):
            node = queue.pop(0)
            level_sum += node.val

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(level_sum / level_size)

    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Level order traversal: " + str(traverse(root)))

    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Reverse level order traversal: " + str(traverse2(root)))

    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.right.left.left = TreeNode(20)
    root.right.left.right = TreeNode(17)
    print("Zigzag traversal: " + str(zigzag(root)))

    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Level averages are: " + str(find_level_averages(root)))

main()
