class Node:
    def __init__(self, val, children = None):
        self.val = val
        self.children = []
        self.depth = 1
        if children is not None:
            for child in children:
                self.add_child(child)
                self.depth = max(child.depth+1, self.depth)
    
    def __repr__(self):
        return str(self.val)

    def print_children(self):
        if self.children:
            print(f'children of {self.val}: [', end ='')
            for child in self.children:
                print(child.val, end=', ')
            print(']')
            for child in self.children:
                child.print_children() 

    def add_child(self, child):
        assert isinstance(child, Node)
        self.children.append(child)
        
    def dfs(self):
        stack = [self]
        while stack:
            curr = stack.pop()
            # in-place
            print(curr)
            for c in curr.children:
                stack.append(c)
