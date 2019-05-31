# WIP, the fucking code
# Maybe WA
N, M = map(int, input().split())

graph_s = []
graph_d = []
trees = []
max_num = 0
for i, _ in enumerate(range(M)):
    # start (smaller num) -> dst (larger num)
    start, dst = map(int, input().split())
    condition_1 = start not in graph_d
    condition_2 = dst in graph_d
    if graph_s == []:  # or graph_d == []
        graph_s.append(start)
        graph_d.append(dst)
    elif condition_1:
        # If the link is discontinuous
        # Add the last graph as "tree"
        trees.append((graph_s, graph_d))
        # Clear and initialize graph
        graph_s.clear()
        graph_d.clear()
        graph_s.append(start)
        graph_d.append(dst)
    elif condition_2:
        # If the graph is not "tree"
        graph_s.clear()
        graph_d.clear()
    else:
        # If the link is continuous
        graph_s.append(start)
        graph_d.append(dst)

    # Update last num
    max_num = max(max_num, dst)

# Count graph that has only a link as tree
n_onelink_tree = 0
if graph_s != []:
    n_onelink_tree += 1

# Count graph that has only a node as tree
n_onenode_tree = N - max_num

print(len(trees) + n_onelink_tree + n_onenode_tree)
