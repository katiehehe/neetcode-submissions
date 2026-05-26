# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        q.append((root, 0))
        final_list = []
        while q:
            x = q.popleft()
            if x[0] is None:
                continue
            if x[1] == len(final_list):
                final_list.append([x[0].val])
            else:
                final_list[x[1]].append(x[0].val)
            q.append((x[0].left, x[1] + 1))
            q.append((x[0].right, x[1] + 1))
        return final_list