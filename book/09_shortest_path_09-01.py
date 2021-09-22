import sys
input = sys.stdin.readline
INF = int(1e9) # 무한을 의미

# 노드의 개수, 간선의 개수를 입력받기
n, m = map(int, input().split())

# 시작 노드 번호를 입력받기
start = int(input())

graph = [[] for i in range(m+1)]

visited = [False] * (n+1)

distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def shortest_path(distance, visited):
    shortest_index = distance.index(min([x for x in distance if x !=0]))
    if not visited[shortest_index]:
        return shortest_index

distance[start] = 0
def save_distance(n):
    for node in graph[n]:
        _node_node = node[0]
        _node_dis = node[1]
        if _node_dis < distance[_node_node] and not visited[_node_node]:
            distance[_node_node] = _node_dis
    visited[n] = True
    return distance, visited

distance, visited = save_distance(1)

index = shortest_path(distance, visited)
