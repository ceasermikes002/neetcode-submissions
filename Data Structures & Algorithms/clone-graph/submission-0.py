from typing import Dict, Optional, List

# ── Step 1: Define the Node with value and neighbors ──────────────────
# Use a class to represent a graph node, including its value and a list of neighbors
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

# ── Step 2: Define the Solution class for graph cloning ──────────────────
# Use a DFS approach to traverse and clone the graph
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:  # handle edge case where input node is None
            return None

        # This dictionary keeps track of all cloned nodes
        cloned_nodes: Dict['Node', 'Node'] = {}

        def dfs(original: 'Node') -> 'Node':
            # Return the clone if it already exists
            if original in cloned_nodes:
                return cloned_nodes[original]
            
            # Clone the node
            clone = Node(original.val)
            cloned_nodes[original] = clone  # map original node to clone
            
            # Clone all the neighbors
            for neighbor in original.neighbors:
                clone.neighbors.append(dfs(neighbor))  # recursive DFS call
            
            return clone

        # Start DFS from the initial node
        return dfs(node)
