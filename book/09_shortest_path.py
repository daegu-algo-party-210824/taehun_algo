node = 6
d_count = 11

graph = [
    [1],
    [1, 2, 2],
    [1, 3, 5],
    [1, 4, 1],
    [2, 3, 3],
    [2, 4, 2],
    [3, 2, 3],
    [3, 6, 5],
    [4, 3, 3],
    [4, 5, 1],
    [5, 3, 1],
    [5, 6, 2],
]

visited = [int(1e9)] * node
visited[0] = 0

# 각 노드 개수 계산
def node_count():
    node_count = [0]
    count = 0
    for i in range(1, node+1):
        for g in graph:
            if g[0] == i:
                count += 1
        node_count.append(count)
        count = 0
    return node_count



print(node_count())




# check_visited()
print(visited)
