class Node:
    def __init__(self, val, ifTerminate, children = None):
        self.val = val
        self.ifTerminate = ifTerminate
        self.children = {}
        self.depth = 1
        if children is not None:
            for child in children:
                self.add_child(child)
                self.depth = max(child.depth+1, self.depth)
    
    def __repr__(self):
        return f'{self.val} {self.ifTerminate}'

    def print_children(self):
        if self.children:
            print(f'children of {self.val}, {self.ifTerminate}: ', end ='')
            print(self.children)
            
            for child in self.children.values():
                child.print_children()

    def add_child(self, child):
        assert isinstance(child, Node)
        if child.val not in self.children:
            self.children[child.val] = child
            return child
        if child.ifTerminate:
            self.children[child.val].ifTerminate = True
        return self.children[child.val]
        
    def dfs(self):
        stack = [self]
        while stack:
            curr = stack.pop()
            # in-place
            print(curr)
            for c in curr.children:
                stack.append(c)
