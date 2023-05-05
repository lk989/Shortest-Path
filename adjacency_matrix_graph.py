
# create an adjacency list graph class to store the data
class Graph:

    # constructor
    def __init__(self, num_of_nodes, directed=True):
        self.m_num_of_nodes = num_of_nodes
        self.m_directed = directed
        self.m_adj_matrix = [[0 for column in range(num_of_nodes)]
                             for row in range(num_of_nodes)]

    # add the edges with their weights
    def add_edge(self, node1, node2, weight):
        self.m_adj_matrix[node1][node2] = weight

        # in case there is an undirected graph
        if not self.m_directed:
            self.m_adj_matrix[node2][node1] = weight
