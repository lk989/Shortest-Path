import networkx as nx


class Stack:
    """(LIFO)"""
    def __init__(self):
        self.list = []

    def push(self, item):
        """Push 'item' onto the stack."""
        self.list.append(item)

    def pop(self):
        """Pop the most recently pushed item from the stack."""
        return self.list.pop()

    def top(self):
        """Return the last element."""
        return self.list[-1]

    def is_empty(self):
        """Returns true if the stack is empty."""
        return len(self.list) == 0


def dfs_stack(graph, start, target):
    # Create a stack for DFS
    stack = Stack()
    # Push the current source node.
    stack.push(start)
    path = []
    while not stack.is_empty():
        # Pop a vertex from stack and print it
        vertex = stack.pop()
        # Stack may contain same vertex twice.
        if vertex in path:
            continue
        # Get all adjacent vertices of the
        # popped vertex s. If a adjacent has not
        # been visited, then push it to the stack.
        path.append(vertex)
        if vertex == target:
            return path
        for neighbor in nx.neighbors(graph, vertex):
            stack.push(neighbor)
    return path
