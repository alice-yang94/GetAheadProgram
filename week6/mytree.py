class Node:
    def __init__(self, val, isTerminate, children = None):
        self.val = val
        self.isTerminate = isTerminate
        self.children = {}
        if children is not None:
            for child in children:
                self.add_child(child)
    
    def __repr__(self):
        return f'{self.val} {self.isTerminate}'

    def print_children(self):
        if self.children:
            print(f'children of {self.val}, {self.isTerminate}: ', end ='')
            print(self.children)
            
            for child in self.children.values():
                child.print_children()

    def add_child(self, child):
        assert isinstance(child, Node)
        if child.val not in self.children:
            self.children[child.val] = child
            return child
        if child.isTerminate:
            self.children[child.val].isTerminate = True
        return self.children[child.val]
        
    def dfs(self):
        stack = [self]
        while stack:
            curr = stack.pop()
            # in-place
            print(curr)
            for c in curr.children:
                stack.append(c)
