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

visited = [int(1e9)] * (node+1)
check = [False] * (node+1)

# count each node list
node_count = [0]
count = 0
for i in range(1, node+1):
    for g in graph:
        if g[0] == i:
            count += 1
    node_count.append(count)
    count = 0


# # find shortest path node
def shortest_node(v, c):
    print(v, c)
    for i in range(0, len(c)):
        if c[i] == True:
            v.remove(v[i])



# 노드별 방문 기록
for i in range(1, node+1):
    for ii in range(0, d_count):
        if len(graph[ii]) == 1:
            visited[graph[ii][0]] = 0

        elif i == graph[ii][0]:
            visited[graph[ii][1]] = graph[ii][2]
    check[i] = True
    min_node = shortest_node(visited, check)










# check_visited()
print(visited)
