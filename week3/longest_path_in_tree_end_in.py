
def longest_path_in_tree(root):
    """
    Returns the length of the longest path of consecutive integers 
    in a tree

    Args:
        root: root of a tree with integers
    """
    # store node with its longest path in stack
    stack = [(root,1)]
    # keep record of current max length
    max_length = 0

    while stack:
        curr, length = stack.pop()
        max_length = max(length, max_length)
        # curr.children returns list of children of curr node
        for child in curr.children:
            child_length = 1
            # propagate longest path length from top to down
            if child.val == curr.val + 1:
                child_length += length
            stack.append((child, child_length))
    return max_length