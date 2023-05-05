from queue import PriorityQueue
from read_data import vertices


# implementation of Best-FS algorithm using priority queue:
def best_first_search_pq(graph, start, end):
    # an array to check whether the vertex has been visited or not
    # this check is important to avoid loops
    visited = [False] * vertices

    # create a priority queue to store the wanted edges
    pq = PriorityQueue()

    # add elements to the priority queue as (cost, node2)
    pq.put((0, start))

    # mark the starting node as visited
    visited[start] = True

    # continue adding the neighbours of the visited node until
    # the queue is empty or the target node is reached
    while not pq.empty():
        # store the node in a variable
        u = pq.get()[1]

        # Displaying the path having the lowest cost
        print(u, end=" ")
        if u == end:
            break

        # add the neighbours of each node to the queue
        for i in range(vertices):
            if graph.m_adj_matrix[u][i] != 0.0 and not visited[i]:
                visited[i] = True
                pq.put((graph.m_adj_matrix[u][i], i))

    print()
