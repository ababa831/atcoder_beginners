# WA
# Test cases: 
from collections import deque


class DFSTool(object):
    def __init__(self, N, graph, init_stack):
        self.N = N 
        self.graph = graph
        self.data_len = len(graph)
        self.stack = deque()
        self.stack.append(init_stack)
        stack_val = 1
        # append src_val of the initial stack
        self.already_passed_nodes = []
        self.already_passed_nodes.append(init_stack[stack_val][0])
        self.n_tree = 0

    def dfs(self):
        curr_idx, link = self.stack.pop()
        # If empty
        if link is None:
            return

        # Be aware of the branch order:
        # You should evaluate "the link is final" at an early stage
        dst_val = link[1]
        if dst_val in self.already_passed_nodes:
            return
        elif not self.next_in_range(curr_idx):
            if dst_val != N:
                self.n_tree += self.N - dst_val + 1
        elif not self.is_continueous(curr_idx, dst_val):
            if self.next_in_range(curr_idx):
                next_src_val = self.graph[curr_idx + 1][0]
                self.n_tree += next_src_val - dst_val
                self.stack_append_next_links(curr_idx, next_src_val)
        else:
            self.stack_append_next_links(curr_idx, dst_val)
            self.already_passed_nodes.append(dst_val)

    def stack_append_next_links(self, cursor_idx, target_val):
        for new_idx, curr_link in enumerate(self.graph[cursor_idx + 1:]):
            if target_val == curr_link[0]:
                self.stack.append([cursor_idx + 1 + new_idx, curr_link])

    def next_in_range(self, target_idx):
        if target_idx + 1 <= self.data_len - 1:
            return True
        else:
            return False

    def is_continueous(self, dst_idx, dst_val):
        # If there is a next link
        if self.next_in_range(dst_idx):
            next_src = self.graph[dst_idx + 1][0]
            if next_src <= dst_val:
                return True
            else:
                return False
        else:
            return False


if __name__ == "__main__":
    # Input
    N, M = map(int, input().split())
    graph = [tuple(map(int, input().split())) for _ in range(M)]
    # DFS
    start_idx = 0
    dfst = DFSTool(N, graph, [start_idx, graph[start_idx]])
    while dfst.stack:
        dfst.dfs()
    # Output
    print(dfst.n_tree)
