"""Given a binary tree, return the zigzag level order traversal of its node’s values.
(ie, from left to right, then right to left for the next level and alternate between).

         3
        / \
    9         20
   / \        /  \
  6  12       15      7
/  \   \     /      /  \
2   8  13   10     16  20


[
  [3],
  [20,9],
  [6,12,15,7]
  [20,16,10,13,8,2]
]
"""
from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value):
    if root is None:
        return TreeNode(value)
    elif value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root

def zigzag_level_order_traversal(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])
    left_to_right = True
    
    while queue:
        level_size = len(queue)
        current_level = deque()
        
        for _ in range(level_size):
            node = queue.popleft()
            
            if left_to_right:
                current_level.append(node.value)
            else:
                current_level.appendleft(node.value)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(list(current_level))
        left_to_right = not left_to_right
    
    return result

# Example Usage
if __name__ == "__main__":
    # Define the root node
    root = TreeNode(3)

    # Insert other nodes
    values = [9, 20, 6, 12, 15, 7, 2, 8, 13, 10, 16, 20]
    for value in values:
        root = insert(root, value)

    # Perform zigzag level order traversal
    result = zigzag_level_order_traversal(root)
    print(result)
