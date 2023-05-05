import time
import random
import pandas as pd
import networkx as nx

import adjacency_matrix_graph

from a_star_hash_table import adjacency_list, H, Graph
from bidirectional_first_search_queue import BidirectionalSearch
from bidirectional_first_search_array import visitedL, visitedR, adjAray, parentL, parentR
from depth_first_search_array import AdjListGraph
import a_star_priority_queue


# a script to read the data from a file and store it in the graph

vertices = 5001
edges = 124666
graph1 = adjacency_matrix_graph.Graph(vertices)
graph2 = a_star_priority_queue.Graph


# read each line and return it at immediately
def read_line(file_name):
    with open(file_name) as file:
        for i in file:
            yield i


def read_weighted_data_adjacency_matrix(graph, type):
    gen = read_line('weighted.txt')
    chunk = [i for i, j in zip(gen, range(edges))]
    for i in chunk:
        # separate the numbers
        tmp = i.split()
        a = int(tmp[0])
        b = int(tmp[1].replace('\n', '').replace('q', ''))
        e = float(tmp[2])
        if type == 1:
            graph.add_edge(a, b, e)
        else:
            graph[a][b] = e
    return graph


def read_weighted_data_nx_graph():
    G = nx.Graph()
    gen = read_line('weighted.txt')
    chunk = [i for i, j in zip(gen, range(edges))]
    for i in chunk:
        tmp = i.split()
        a = int(tmp[0])
        b = int(tmp[1].replace('\n', '').replace('q', ''))
        w = float(tmp[2].replace('\n', '').replace('q', ''))
        G.add_edge(a, b, weight=w)
    return G


def read_weighted_data_adj_list():
    for i in range(vertices + 1):
        adjacency_list[str(i)] = []

    gen = read_line('weighted.txt')
    chunk = [i for i, j in zip(gen, range(edges))]
    for i in chunk:
        tmp = i.split()
        a = tmp[0]
        b = tmp[1].replace('\n', '').replace('q', '')
        w = float(tmp[2].replace('\n', '').replace('q', ''))
        adjacency_list[a].append((b, w))
        if ~(a in H):
            n = random.randint(10, 100)
            H[a] = n
        if ~(b in H):
            n = random.randint(10, 100)
            H[b] = n


def read_unweighted_data_nx_graph():
    G = nx.Graph()
    gen = read_line('unweighted.txt')
    chunk = [i for i, j in zip(gen, range(edges))]
    for i in chunk:
        tmp = i.split()
        a = int(tmp[0])
        b = int(tmp[1].replace('\n', '').replace('q', ''))
        G.add_edge(a, b)
    return G


def read_unweighted_data_pd_list(graph):
    data = pd.read_csv('unweighted.txt', sep="\t")
    data.columns = ["N1", "N2"]
    n = data["N2"].max()
    for i, j in zip(data["N1"].to_list(), data["N2"].to_list()):
        graph.add_edge(i, j)


def read_unweighted_data_pd_matrix():
    data = pd.read_csv("unweighted.txt", sep="\t", )
    data.columns = ["N1", "N2"]
    n = data["N2"].max()

    for i, j in zip(data["N1"].to_list(), data["N2"].to_list()):
        adjAray[i - 1][j - 1] = j - 1
        adjAray[j - 1][i - 1] = j - 1
    for i in range(n):
        visitedL[i] = False
        visitedR[i] = False
        parentL[i] = -1
        parentR[i] = -1


def read_unweighted_data_adj_list():
    graph = AdjListGraph(10000)
    myset = set()
    lines_required = 300000
    gen = read_line('unweighted.txt')
    chunk = [i for i, j in zip(gen, range(lines_required))]
    for i in chunk:
        tmp = i.split()
        a = int(tmp[0])
        b = int(tmp[1].replace('\n', '').replace('q', ''))
        graph.add_edge(a, b)
    return graph


print('Reading the data ...\n')

start = time.process_time()
graph_adjacency_matrix = read_weighted_data_adjacency_matrix(graph1, 1)
wam_time = time.process_time() - start
print('It took ' + str(wam_time) + ' seconds to read and store the weighted data in an adjacency matrix\n')

graph_adjacency_matrix_2 = read_weighted_data_adjacency_matrix(graph2, 2)

start = time.process_time()
graph_weighted_nx = read_weighted_data_nx_graph()
nx_w_time = time.process_time() - start
print('It took ' + str(nx_w_time) + ' seconds to read and store the weighted data in an nx graph\n')

read_weighted_data_adj_list()
graph_weighted_l = Graph(adjacency_list)

start = time.process_time()
graph_unweighted_nx = read_unweighted_data_nx_graph()
nx_un_time = time.process_time() - start
print('It took ' + str(nx_un_time) + ' seconds to read and store the unweighted data in an nx graph\n')

graph_unweighted_pd_list = BidirectionalSearch(5001)
start = time.process_time()
read_unweighted_data_pd_list(graph_unweighted_pd_list)
pd_un_time = time.process_time() - start
print('It took ' + str(pd_un_time) + ' seconds to read and store the unweighted data in a list using panda libraries\n')

start = time.process_time()
read_unweighted_data_pd_matrix()
pd_un_time = time.process_time() - start
print('It took ' + str(pd_un_time) + ' seconds to read and store the unweighted data in a matrix using panda '
                                     'libraries\n')

start = time.process_time()
graph_unweighted_l = read_unweighted_data_adj_list()
l_un_time = time.process_time() - start
print('It took ' + str(l_un_time) + ' seconds to read and store the unweighted data in an adjacent list\n')
