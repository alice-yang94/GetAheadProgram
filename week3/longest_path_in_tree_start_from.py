"""
This method propagates longest length bottom up.
The intuition is finding the longest path starts from each node.
However, top down approach can already solve this problem which 
can be seen as the longest path ends in each node. 
See longest_path_in_tree_end_in.py for detail
"""
from collections import defaultdict

def longest_path_in_tree(root):
    # stack store nodes in dfs order, O(n) space
    stack = [root]
    # store visited elements as a set since all node are unique,
    # O(1) lookup, O(n) space
    visited = set()
    # a dictionary to store node value and longest length pairs
    # O(1) lookup, O(n) space
    node_to_len = defaultdict(int)

    """
    Push nodes in the tree in DFS order, then, propogate the longest 
    length bottom up.
    """
    while stack:
        curr = stack.pop()
        if curr not in visited:
            visited.add(curr)
            stack.append(curr)
            for child in curr.children:
                stack.append(child)
        else:
            has_consecutive_child = False
            # add longest length from child to curr node
            for c in curr.children:
                if curr.val+1 == c.val:
                    node_to_len[curr.val] += node_to_len[c.val] + 1
                    has_consecutive_child = True
                    # each int only appear once, at most one child 
                    # would be the consecutive path
                    break
            if not has_consecutive_child:
                node_to_len[curr.val] = 1
    print(node_to_len)
    return max(node_to_len.values())