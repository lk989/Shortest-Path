import numpy as np

n = 5000
adjAray = -1 * np.ones(shape=(n, n), dtype="object")
visitedR = np.empty(shape=n, dtype="object")
visitedL = np.empty(shape=n, dtype="object")
parentR = np.zeros(shape=n, dtype="object")
parentL = np.zeros(shape=n, dtype="object")

def bidirectional_search(s, t):
    def extract_path(node):
        """return the path when both BFS's have met"""
        node_copy = node
        path = []
        while node != -1:
            path.append(node)
            node = parentR[node]
        path.reverse()
        del path[-1]  # because the meeting node appears twice
        while node_copy != -1:
            path.append(node_copy)
            node_copy = parentL[node_copy]
        return path

    q = []
    q.append(s)
    q.append(t)
    visitedR[s] = True
    visitedL[t] = True
    while len(q) != 0:
        n = q.pop(0)
        if visitedL[n] and visitedR[n]:  # if the node visited by both BFS's
            print("\nThe intersection point is:", n + 1)
            return extract_path(n)
        for node in adjAray[n]:
            if node != -1:
                if visitedL[n] == True and not visitedL[node]:
                    parentL[node] = n
                    visitedL[node] = True
                    q.append(node)
                if visitedR[n] == True and not visitedR[node]:
                    parentR[node] = n
                    visitedR[node] = True
                    q.append(node)

    return False


