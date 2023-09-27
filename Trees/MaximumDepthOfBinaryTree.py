"""
Author: bala1802@live.com
GitHub: github.com/bala1802
"""

import collections

class TreeNode:

    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    """
    Recursive Depth First Search: INORDER DFS
    The Time complexity will be O(n); and the Space complexity will be O(n) - n is the maximum depth of the binary tree
    """
    def maxDepth(self, root):

        if root is None:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    
    """
    Breadth First Search approach
    """
    def bfsApproach(self, root):
        
        if root is None:
            return 0
        
        level = 0
        queue = collections.deque([root])

        while queue:
            """
            Traversing all the elements present in the Level
            """
            for i in range(len(queue)):
                """
                    - i is the level Id
                    - node left and right are the elements present in that level we are currently accessing
                """
                node = queue.popleft()
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
                
            
            level += 1
                
        
        return level

    """
    Iterative Depth First Search: PreOrder Traversal
    - Process the root
    - Process the left child
    - Process the right child

    """
    def iterativeDfs(self, root):
        stack = [[root, 1]]
        result = 0
        
        while stack:
            node, depth = stack.pop()
            if node:
                result = max(result, depth)

                stack.append([node.left, depth+1])
                stack.append([node.right, depth+1])
        
        return result