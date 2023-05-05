from read_data import graph_unweighted_nx

lang_dictionary = {}
lang_tuples = graph_unweighted_nx.edges

# converting a list of the tuple to the dictionary
for lang, value in lang_tuples:
    # list of tuples to the dictionary
    lang_dictionary.setdefault(lang, []).append(value)

def bfs(lang_dictionary, lang_tuples, node, target):
    lang_dictionary.append(node)
    queue = []
    queue.append(node)
    while queue:
        s = queue.pop(0)
        print(s, end=' ')
        if s == target:
            return
        for neighbour in lang_tuples[s]:
            if neighbour not in lang_dictionary:
                lang_dictionary.append(neighbour)
                queue.append(neighbour)
    print()
