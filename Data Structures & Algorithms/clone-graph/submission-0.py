"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        stack = [node]
        if node is None:
            return None
        new_node = Node(node.val)
        new_nodes = {1: new_node}
        while stack:
            top = stack.pop()
            for neigh in top.neighbors:
                if neigh.val not in new_nodes:
                    new_node = Node(neigh.val)
                    new_nodes[neigh.val] = new_node
                    stack.append(neigh)
                    (new_nodes[top.val]).neighbors.append(new_node)
                else:
                    (new_nodes[top.val]).neighbors.append(new_nodes[neigh.val])
        return new_nodes[1]

            
