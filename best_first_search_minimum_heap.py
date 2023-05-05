import sys
from read_data import vertices


# create a minimum heap class to implement the algorithm using it
class MinHeap:

    # constructor
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.Heap = [[] for i in range(maxsize)]
        self.Heap[0] = -1 * sys.maxsize
        self.FRONT = 0

    # get the index of the parent
    def parent(self, pos):
        return pos // 2

    # get the index of the left child
    def leftChild(self, pos):
        return 2 * pos

    # get the index of the right child
    def rightChild(self, pos):
        return (2 * pos) + 1

    # check whether the element is leaf or not
    def isLeaf(self, pos):
        return pos * 2 > self.size

    # swap 2 elements
    def swap(self, fpos, spos):
        self.Heap[fpos], self.Heap[spos] = self.Heap[spos], self.Heap[fpos]

    # an algorithm to maintain the minimum heap order
    def minHeapify(self, pos):

        # If the node is a non-leaf node and greater than any of its children
        if not self.isLeaf(pos):
            # if the node has both children
            if self.Heap[self.leftChild(pos)] and self.Heap[self.rightChild(pos)]:
                if (self.Heap[pos][2] > self.Heap[self.leftChild(pos)][2] or
                        self.Heap[pos][2] > self.Heap[self.rightChild(pos)][2]):

                    # Swap with the left child and heapify the left child
                    if self.Heap[self.leftChild(pos)][2] <\
                            self.Heap[self.rightChild(pos)][2]:
                        self.swap(pos, self.leftChild(pos))
                        self.minHeapify(self.leftChild(pos))

                    # Swap with the right child and heapify the right child
                    else:
                        self.swap(pos, self.rightChild(pos))
                        self.minHeapify(self.rightChild(pos))

            # if the node has only left child
            elif self.Heap[self.leftChild(pos)]:
                if self.Heap[pos][2] > self.Heap[self.leftChild(pos)][2]:
                    self.swap(pos, self.leftChild(pos))

            # if the node has only right child
            elif self.Heap[self.rightChild(pos)]:
                if self.Heap[pos][2] > self.Heap[self.rightChild(pos)][2]:
                    self.swap(pos, self.rightChild(pos))

    # Function to insert a node into the heap
    def insert(self, element):
        # make sure not to acceed the maximum size
        if self.size >= self.maxsize:
            return

        # insert the element
        self.Heap[self.size] = element

        current = self.size
        self.size += 1

        # place the new element in the right place
        while self.Heap[current][2] < self.Heap[self.parent(current)][2]:
            self.swap(current, self.parent(current))
            current = self.parent(current)

    # function to build the min heap using the minHeapify function
    def minHeap(self):
        for pos in range(self.size // 2, 0, -1):
            self.minHeapify(pos)

    # Function to remove and return the minimum element from the heap
    def remove(self):
        popped = self.Heap[self.FRONT]
        self.Heap[self.FRONT] = self.Heap[self.size - 1]
        self.Heap[self.size - 1] = []
        self.size -= 1
        self.minHeapify(self.FRONT)
        return popped

    # implementation of Best-FS algorithm using minimum heap:
    def best_first_search_minheap(self, graph, start, end):
        # an array to check whether the vertex has been visited or not
        # this check is important to avoid loops
        visited = [False] * vertices

        # add all neighbours of the starting node as
        # ([node1, node2, cost])
        for i in range(vertices):
            if graph.m_adj_matrix[start][i] != 0.0 and not visited[i]:
                visited[i] = True
                self.insert([start, i, graph.m_adj_matrix[start][i]])
        print(start, end=' ')

        # continue adding the neighbours of the visited node until
        # the queue is empty or the target node is reached
        while not self.size == 0:
            u = self.Heap[self.FRONT][1]
            # Displaying the path having the lowest cost
            print(u, end=" ")
            self.remove()
            if u == end:
                break

            # add the neighbours of each node to the queue
            for i in range(vertices):
                if graph.m_adj_matrix[u][i] != 0.0 and not visited[i]:
                    visited[i] = True
                    self.insert([start, i, graph.m_adj_matrix[u][i]])
        print()
        if u != end:
            print('There is no path')
