import time
from bidirectional_first_search_array import bidirectional_search
from read_data import *

from breadth_first_search_queue import BFS
from breadth_first_search_dictionary import bfs

from depth_first_search_stack import dfs_stack
import depth_first_search_array

from best_first_search_priorty_queue import best_first_search_pq
import best_first_search_minimum_heap as mh
import best_first_search_btree as bt

from bidirectional_first_search_queue import BidirectionalSearch

from a_star_priority_queue import astar
from a_star_hash_table import Graph


def breadth_first_search(graph):
    print('__________________________________________________________________')
    print('We have chosen 2 data structures for this algorithm. Queue and Dictionary.\n\n'
          'Please choose the start node to find the shortest path using Breadth-First search.\n')
    source = int(input('Enter the starting node "Range is (1-5000)" : '))
    target = int(input('Enter the target node "Range is (1-5000)" : '))
    print('__________________________________________________________________')
    print('1- Queue:\nThe path: ', end='')
    start = time.process_time()
    BFS(graph, source, target)
    q_time = time.process_time() - start
    print('\nIt took ' + str(q_time) + ' seconds to find the path')
    print('__________________________________________________________________')
    print('1- Dictionary:\nThe path: ', end='')
    start = time.process_time()
    bfs([], graph, source, target)
    d_time = time.process_time() - start
    print('\nIt took ' + str(d_time) + ' seconds to find the path')
    print('__________________________________________________________________')

    if q_time < d_time:
        print('Queue is the best data structure for Breadth First Search since it has the minimum time')
    else:
        print('Dictionary is the best data structure for Breadth First Search since it has the minimum time')
    print('__________________________________________________________________')


def depth_first_search(graph_nx, graph_l):
    print('__________________________________________________________________')
    print('We have chosen 2 data structures for this algorithm. Stack and Array.\n\n'
          'Please choose the start and target nodes to find the shortest path between them using Depth First search.\n')
    source = int(input('Enter the starting node "Range is (1-5000)" : '))
    target = int(input('Enter the target node "Range is (1-5000)" : '))
    print('__________________________________________________________________')
    print('1- Stack:\nThe path: ', end='')
    start = time.process_time()
    path = dfs_stack(graph_nx, source, target)
    print(path)
    s_time = time.process_time() - start
    print('It took ' + str(s_time) + ' seconds to find the path')
    print('__________________________________________________________________')
    print('2- Array:\nThe path: ', end='')
    start = time.process_time()
    path = []
    path = depth_first_search_array.AdjListGraph.dfs(graph_l, source, target)
    print(path)
    print(time.process_time() - start)
    a_time = time.process_time() - start
    print('It took ' + str(a_time) + ' seconds to find the path')
    print('__________________________________________________________________')

    if s_time < a_time:
        print('Stack is the best data structure for Depth first search Search since it has the minimum time')
    else:
        print('Array is the best data structure for Depth first search Search since it has the minimum time')

    print('__________________________________________________________________')
    return


def best_first_search(graph):
    print('__________________________________________________________________')
    print('We have chosen 3 data structures for this algorithm. Priority Queue, Minimum Heap and Binary Tree.\n\n'
          'Please choose the start and target nodes to find the shortest path between them using Best-First search.\n')
    source = int(input('Enter the starting node "Range is (1-5000)" : '))
    target = int(input('Enter the target node "Range is (1-5000)" : '))
    print('__________________________________________________________________')
    print('1- Priority Queue:\nThe path: ', end='')
    start = time.process_time()
    best_first_search_pq(graph, source, target)
    pq_time = time.process_time() - start
    print('It took ' + str(pq_time) + ' seconds to find the path')
    print('__________________________________________________________________')
    print('2- Minimum Heap:\nThe path: ', end='')
    start = time.process_time()
    heap = mh.MinHeap(vertices)
    start = time.process_time()
    heap.best_first_search_minheap(graph, source, target)
    mh_time = time.process_time() - start
    print('It took ' + str(mh_time) + ' seconds to find the path')
    print('__________________________________________________________________')
    print('3- Binary Tree:\nThe path: ', end='')
    start = time.process_time()
    tree = None
    start = time.process_time()
    bt.best_s(graph, tree, source, target)
    bt_time = time.process_time() - start
    print('It took ' + str(bt_time) + ' seconds to find the path')
    print('__________________________________________________________________')

    if pq_time < bt_time and pq_time < mh_time:
        print('Priority Queue is the best data structure for Best-First Search since it has the minimum time')
    elif mh_time < bt_time and mh_time < pq_time:
        print('Minimum Heap is the best data structure for Best-First Search since it has the minimum time')
    else:
        print('Binary Tree is the best data structure for Best-First Search since it has the minimum time')

    print('__________________________________________________________________')


def bidirectional_first_search(graph):
    print('__________________________________________________________________')
    print('We have chosen 2 data structures for this algorithm. Queue and Array.\n\n'
          'Please choose the start and target nodes to find the shortest path using Bidirectional-First search.\n')
    source = int(input('Enter the starting node "Range is (1-5000)" : '))
    target = int(input('Enter the end node "Range is (1-5000)" : '))
    print('__________________________________________________________________')
    print('1- Queue:\nThe path: ', end='')
    start = time.process_time()
    path = BidirectionalSearch.bidirectional_search(graph, source, target)
    if path == -1:
        print(f"Path does not exist between {source} and {target}")
    q_time = time.process_time() - start
    print('It took ' + str(q_time) + ' seconds to find the path')
    print('__________________________________________________________________')
    print('1- Array:\nThe path: ', end='')
    start = time.process_time()
    path = bidirectional_search(source - 1, target - 1)
    if path is not False:
        print(f"A Path does exist between {source} and {target}")
        print(*[">>{}".format(i + 1) for i in path])
        print(f"")
    else:
        print(f"Path does not exist between {source} and {target}")
    a_time = time.process_time() - start
    print('It took ' + str(a_time) + ' seconds to find the path')
    print('__________________________________________________________________')

    if q_time < a_time:
        print('Queue is the best data structure for Bidirectional first search Search since it has the minimum time')
    else:
        print('Array is the best data structure for Bidirectional first search Search since it has the minimum time')

    print('__________________________________________________________________')


def a_star(graph1, graph2):
    print('__________________________________________________________________')
    print('We have chosen 2 data structures for this algorithm. Priority Queue and Hash Table.\n\n'
          'Please choose the start and target nodes to find the shortest path between them using A* search.\n')
    input_source = input('Enter the starting node "Range is (1-5000)" : ')
    input_target = input('Enter the target node "Range is (1-5000)" : ')
    source = (int(input_source), 10)
    target = (int(input_target), 0)
    print('__________________________________________________________________')
    print('1- Priority Queue:\nThe path: ', end='')
    start = time.process_time()
    path = astar(graph1, source, target)
    print(path)
    pq_time = time.process_time() - start
    print('It took ' + str(pq_time) + ' seconds to find the path')
    print('__________________________________________________________________')
    print('2- Hash Table:\nThe path: ', end='')
    start = time.process_time()
    path = Graph.a_star_algorithm(graph2, input_source, input_target)
    print(path)
    ht_time = time.process_time() - start
    print('It took ' + str(ht_time) + ' seconds to find the path')
    print('__________________________________________________________________')

    if pq_time < ht_time:
        print('Priority Queue is the best data structure for A* Search since it has the minimum time')
    else:
        print('Hash Table is the best data structure for A* Search since it has the minimum time')

    print('__________________________________________________________________')


def main():
    print('__________________________________________________________________')
    print('                          Shortest Path')
    print('__________________________________________________________________')

    algorithm = 6

    while algorithm != 0:
        print('1: BFS "Breadth First Search"\n2: DFS "Depth First Search"\n3: Best First Search'
              '\n4: Bidirectional First Search\n5: A* Algorithm')
        print('__________________________________________________________________')
        algorithm = int(input('Choose which algorithm you want to use or 0 to quit: '))

        if algorithm == 0:
            quit()
        elif algorithm == 1:
            breadth_first_search(graph_unweighted_nx)
        elif algorithm == 2:
            depth_first_search(graph_unweighted_nx, graph_unweighted_l)
        elif algorithm == 3:
            best_first_search(graph_adjacency_matrix)
        elif algorithm == 4:
            bidirectional_first_search(graph_unweighted_pd_list)
        elif algorithm == 5:
            a_star(graph_adjacency_matrix_2, graph_weighted_l)
        else:
            print('Invalid choice. Please choose again.')


if __name__ == '__main__':
    main()
