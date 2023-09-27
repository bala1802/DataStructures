class TreeNode:

    def __init__(self, val=0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
    

class Solution:

    def invertTree(self, root):
        
        if root is None:
            return None
        
        root.left, root.right = root.right, root.left

        self.invertTree(root = root.left)
        self.invertTree(root = root.right)
        
        return root
