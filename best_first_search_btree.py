# Binary Tree in Python
from read_data import vertices


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, data):
    if root is None:
        return Node(data)
    else:
        if root.data[1] == data[1]:
            return root
        elif root.data[1] < data[1]:
            root.right = insert(root.right, data)
        else:
            root.left = insert(root.left, data)
    return root


def min_value_node(node):
    if node is None:
        return node
    current = node
    while current.left is not None:
        current = current.left
    return current


def print_inorder(root):
    if root is not None:
        print_inorder(root.left)
        print(root.data[1], end=" ")
        print_inorder(root.right)


def delete_node(root, key):
    if root is None:
        return root

    if key < root.data[1]:
        root.left = delete_node(root.left, key)
    elif key > root.data[1]:
        root.right = delete_node(root.right, key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp

        temp = min_value_node(root.right)
        root.data[1] = temp.data[1]
        root.right = delete_node(root.right, temp.data[1])

    return root


def best_s(graph, root, start, end):
    visited = [False] * vertices
    root = insert(root, [start, 0])
    visited[start] = True

    while root is not None:
        u = min_value_node(root).data[0]
        print(u, end=' ')
        if u == end:
            break
        root = delete_node(root, min_value_node(root).data[1])
        for i in range(vertices):
            if graph.m_adj_matrix[u][i] != 0.0 and not visited[i]:
                root = insert(root, [i, graph.m_adj_matrix[u][i]])
                visited[i] = True

    print()
