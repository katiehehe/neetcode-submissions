# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def lowest_helper(root):
            if p.val < root.val and q.val < root.val:
                return lowest_helper(root.left)
            if p.val > root.val and q.val > root.val:
                return lowest_helper(root.right)
            return root
        return lowest_helper(root)