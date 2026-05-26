# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid_helper(root, min_val, max_val):
            if root is None:
                return True
            if root.val >= max_val or root.val <= min_val:
                return False
            return (valid_helper(root.left, min_val, min(root.val, max_val))
                and valid_helper(root.right, max(root.val, min_val), max_val))
        return valid_helper(root, -float('inf'), float('inf'))
        