# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def augment(root):
            if root is None:
                return 0
            root.size = 1 + augment(root.left) + augment(root.right)
            return root.size
        # augment the tree
        augment(root)
        def kth_helper(root, k):
            # do range queries
            left_size = root.left.size if root.left is not None else 0
            if k < left_size + 1:
                return kth_helper(root.left, k)
            if k == left_size + 1:
                return root.val
            return kth_helper(root.right, k - left_size - 1)
        return kth_helper(root, k)

