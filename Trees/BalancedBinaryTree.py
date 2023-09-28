class TreeNode:

    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def isBalanced(self, root) -> bool:
        def depth_first_search(root):
            if root is None:
                return [True, 0]
            
            left, right = depth_first_search(root.left), depth_first_search(root.right)
            balanced = left[0] and right[0] and abs(left[1]-right[1]) <= 1

            return [balanced, 1+max(left[1], right[1])]

        return depth_first_search(root)[0]