
class AdjListGraph:
    # Constructor
    def __init__(self, num_of_nodes, directed=True):
        self.m_num_of_nodes = num_of_nodes
        self.m_nodes = range(self.m_num_of_nodes)

        # Directed or Undirected
        self.m_directed = directed

        # Graph representation - Adjacency list
        # We use a dictionary to implement an adjacency list
        self.m_adj_list = {node: set() for node in self.m_nodes}

        # Add edge to the graph

    def add_edge(self, node1, node2):
        self.m_adj_list[node1].add(node2)

    def dfs(self, start, target, path=[], visited=set()):
        # added the start node to the beginning of our traversal path
        # and marked it as visited by adding it to a set of visited nodes
        path.append(start)
        visited.add(start)

        if start == target:
            return path
        for (neighbour) in self.m_adj_list[start]:
            if neighbour not in visited:
                result = self.dfs(neighbour, target, path, visited)
                if result is not None:
                    return result
        path.pop()
        return None
