class TreeNode:

    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    """
    Deprecated
    """
    def isSameTree(self, p, q):

        def dfs(nodeP, nodeQ):
            if nodeP is None and nodeQ is None:
                return True
            
            if nodeP is None or nodeQ is None or nodeP.val != nodeQ.val:
                return False
            
            return dfs(nodeP.left, nodeQ.left) and dfs(nodeP.right, nodeQ.right)
        
        return dfs(nodeP = p, nodeQ = q)
    
    """
    Optimized Solution
    """

    def isSameTree(self, p, q):
        if p is None and q is None:
            return False
        
        if p is None or q is None or p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
                
            

