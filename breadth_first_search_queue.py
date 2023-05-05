
def BFS(graph, node, target):
    visited = []  # List for visited nodes.
    visited.append(node)
    queue = []
    queue.append(node)

    while queue:
        s = queue.pop(0)
        print(s, end=' ')

        if s == target:
            return

        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
    print()

