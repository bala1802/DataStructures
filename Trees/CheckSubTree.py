class TreeNode:

    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:

    def isSubTree(self, source, target):
        if target is None:
            return True
        if source is None:
            return False
        if self.sameTree(source, target):
            return True
        return self.isSubTree(source=source.left, target=target) or self.isSubTree(source=source.left, target=target)
        
    def sameTree(self, source, target):
        if source is None and source is None:
            return True
        
        if source is not None and target is not None and source.val == target.val:
            return self.sameTree(source.left, target.left) and self.sameTree(source.right, target.right)
        return False
            
        
        