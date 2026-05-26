# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        positions = {}
        n = len(preorder)
        for idx, elem in enumerate(inorder):
            positions[elem] = idx
        def helper(p1, p2, i1, i2):
            if p1 == p2:
                return None
            pos = positions[preorder[p1]]
            return TreeNode(preorder[p1], helper(p1+1, p1+1+pos-i1, i1, pos), helper(p1+1+pos-i1, p2, pos+1, i2))
        return helper(0, n, 0, n)