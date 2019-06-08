from collections import deque
from copy import copy


class DFSTool(object):
    def __init__(self, cursor, links, start_node, M):
        self.cursor = cursor
        self.next_cursor = 0
        self.links = links
        self.M = M
        self.stack = deque()
        self.stack.append(start_node)
        self.already_passed_nodes = []
        self.is_not_graph = False
        self.last_dst = 0
        self.n_tree = 0

    def DFS(self):
        src = self.stack.pop()
        if src in self.already_passed_nodes:
            self.is_not_graph = True
            return
        else:
            for idx, link in enumerate(self.links[self.cursor:]):
                if src == link[0]:
                    # Append next src
                    self.stack.append(link[1])
                    # The fucking code
                    self.next_cursor = idx + self.cursor + 1
                    self.last_dst = max(self.last_dst, link[1])
            self.already_passed_nodes.append(src)

    def move2next_graph(self):
        if self.next_cursor < M:
            next_init_src = self.links[self.next_cursor][0]

            # Count num_trees
            if self.is_not_graph:
                self.n_tree += next_init_src - self.last_dst - 1
            else:
                self.n_tree += next_init_src - self.last_dst

            # Move to next graph
            self.cursor = copy(self.next_cursor)
            self.already_passed_nodes = []
            self.is_not_graph = False
            self.stack.clear()
            self.stack.append(next_init_src)


if __name__ == "__main__":
    # Input
    N, M = map(int, input().split())
    links = [tuple(map(int, input().split())) for _ in range(M)]
    # DFS
    init_cursor = 0
    init_src = links[0][0]
    dfst = DFSTool(init_cursor, links, init_src, M)
    while dfst.next_cursor < M:
        while dfst.stack:
            dfst.DFS()
            if dfst.is_not_graph:
                break
        dfst.move2next_graph()
    # If the cursol arrived at the last element of "links"
    if dfst.is_not_graph:
        dfst.n_tree += N - dfst.last_dst
    else:
        dfst.n_tree += N - dfst.last_dst + 1
    # Output
    print(dfst.n_tree)
