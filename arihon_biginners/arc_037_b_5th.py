# WA
# All examples were passed, but WA in some test cases
from collections import deque


class DFSTool(object):
    def __init__(self, node, connect=[]):
        self.connect = connect
        self.queue = deque()
        self.already_passed = []
        self.not_tree = False
        self.n_tree = 0
        self.node = node
        self.queue.append(node)

    def append(self, search_nodes):
        for s_node in search_nodes:
            self.queue.append(s_node)

    def DFS(self):
        node = self.queue.popleft()
        if node in self.already_passed:
            return
        if node in self.queue:
            self.not_tree = True
        self.append(self.connect[node - 1])
        self.already_passed.append(node)
        self.node = node  # For jump2next

    def jump2next(self):
        """Use this method if the queue is empty"""
        if self.not_tree is False:
            self.n_tree += 1
        self.node += 1
        self.queue.append(self.node)
        self.not_tree = False  # Reset flag


if __name__ == "__main__":
    # Input
    N, M = map(int, input().split())
    connect = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        connect[u - 1].append(v)
        connect[v - 1].append(u)
    # DFS
    search_node = 1
    dfst = DFSTool(search_node, connect=connect)
    while dfst.node <= N:
        dfst.DFS()
        # For print debug
        # print('queue: ', dfst.queue)
        # print('s_node:', dfst.node, ', n_tree:', dfst.n_tree)
        if not dfst.queue:
            dfst.jump2next()
    print(dfst.n_tree)
