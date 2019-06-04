# WIP
from collections import deque


class DFSTool(object):
    def __init__(self, graph, tuple_init_stack):
        self.graph = graph
        self.data_len = len(graph)
        self.stack = deque()
        self.stack.append(tuple_init_stack)
        self.already_passed_nodes.append(tuple_init_stack[0])

    def dfs(self):
        link = self.stack.pop()
        if link is None:
            return

        dst = link[1]
        next_idxes = self._dst_in_srcs(dst)
        if dst in self.already_passed_nodes:
            return
        elif next_idxes == []:
            return
        else:
            for next_idx in next_idxes:
                self.stack.append(self.graph[next_idx])
            self.already_passed_nodes.append(dst)

    def _dst_in_srcs(self, dst):
        idxes = []
        for idx, val in enumerate(self.graph):
            tmp_src = val[0]
            if dst in tmp_src:
                idxes.append(idx)
        return idxes


if __name__ == "__main__":
    # Input
    N, M = map(int, input().split())
    graph = [tuple(map(int, input().split())) for _ in range(M)]
    # DFS
    dfst = DFSTool(graph, graph[0])
    while dfst.stack:
        dfst.dfs()

    # TODO: Deal with discontinuous tree (How to reset DFS)
