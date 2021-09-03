def stack_theory():
    # 자료구조의 기초 stack 예제
    stack = []
    stack.append(5) # 5
    stack.append(2) # 5 2
    stack.append(3) # 5 2 3
    stack.append(7) # 5 2 3 7
    stack.pop()     # 5 2 3
    stack.append(1) # 5 2 3 1
    stack.append(4) # 5 2 3 1 4
    stack.pop()     # 5 2 3 1
    print(stack)

def queue_theory():
    # 자료구조의 기초 queue 예제
    from collections import deque

    queue = deque()
    queue.append(5) # 5
    queue.append(2) # 2 5
    queue.append(3) # 3 2 5
    queue.append(7) # 7 3 2 5
    queue.popleft() # 7 3 2
    queue.append(1) # 1 7 3 2
    queue.append(4) # 4 1 7 3 2
    queue.popleft() # 4 1 7 3

    print(queue)    # 입력된 순서대로 출력
    queue.reverse()
    print(queue)    # 나중에 들어온 원소부터 출력

def recursive_func_01():
    # DFS와 BFS를 구현하기 위해 필요한 재귀 함수 예제 1, 재귀함수 이해
    '''
    RecursionError: maximum recursion depth exceeded
    while calling a Python object
    와 같은 에러 발생 하게 된다. 즉, 재귀의 최대 깊이를 초과했다는 내용이다.
    '''
    # recursive_function
    print('재귀 함수 호출')
    recursive_func_01()

def recursive_func_02(i=1):
    # DFS와 BFS를 구현하기 위해 필요한 재귀 함수 예제 2
    # 이번 예제에서는 재귀함수과 스택 자료구조와 같다는 것을 확인 할 수 있다.
    # 즉, 마지막 번째 함수가 수행되고 난 후 종료(pop)되는 것을 확인 할 수 있다.
    if i == 100:
        return
    print(f'{i}번째 재귀 함수에서, {i+1}번째 재귀 함수를 호출합니다.')
    recursive_func_02(i+1)
    print(f'{i}번째 재귀 함수를 종료합니다.')

def recursive_func_03(n):
    # 팩토리얼 문제를 구현
    # 재귀 함수를 이용하면 수학의 점화식 처럼 코드를 작성 가능하여 간결하다.
    if n <= 1:
        return 1
    return n * recursive_func_03(n-1)

def adjacency_matrix():
    # 모든 관계 저장
    # 메모리 낭비 but 정보를 얻는 속도가 인접 리스트 보다 좋음
    INF = 9999999

    # 2차원 리스트를 이용해서 인접 행렬 표현
    graph = [
        [0, 7, 5],
        [7, 0, INF],
        [5, INF, 0]
    ]

    print(graph)

def adjanceny_list():
    # 인접 리스트 방식은 연결된 데이터를 하나씩 확인해야하기 때문에 검색이 느린 반면
    # 연결되어 있는 정보만 저장하기 때문에 메모리를 효율적으로 사용

    # row 3개 만들기
    graph = [[] for _ in range(3)]

    # 노드 0에 연결된 노드 정보
    graph[0].append((1, 7))
    graph[0].append((2, 5))

    # 노드 1에 연결된 노드 정보
    graph[1].append((0, 7))

    # 노드 2에 연결된 노드 정보
    graph[2].append((0, 5))

    print(graph)

def dfs_basic(graph, visited, v):

    # 방문 처리
    visited[v] = True
    print(v, end= ' ')

    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs_basic(graph, visited, i)

def bfs_basic(graph, start, visited):
    # parameters example
    # graph = [
    #     [],
    #     [2, 3, 8],
    #     [1, 7],
    #     [4, 5],
    #     [3, 5],
    #     [3, 4],
    #     [7],
    #     [2, 6, 8],
    #     [1, 7]
    # ]
    # start = 1
    # visited = [False] * 9
    from collections import deque

    queue = deque([start])

    #방문 처리
    visited[start] = True

    # 큐가 비워 질 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

def freeze_drinks(n, m, ice_shape):
    # 실전문제 음료수 얼려 먹기

    # 0의 row 위치파악
    # stack_list = []
    # for num in range(n):
    #     for i in ice_shape[num]:
    #         if i == 0:
    #             stack_list.append(i)
    for i in range(n):
        for ii in range(m):
            try:
                up = ice_shape[i-1][ii] # 상
                left = ice_shape[i][ii-1]  # 좌
                down = ice_shape[i+1][ii] # 하
                right = ice_shape[i][ii+1] # 우
                original = ice_shape[i][ii]
            except:
                up = 0
                left = 0

            if original == 0:
                if up == 0 and left == 0 and down == 0 and right == 0 :
                    print('a')

                if up == 1 and left == 1 and down == 1 and right == 1 :
                    print('b')


n = 4
m = 5
ice_shape = [
    [0, 0, 1, 1, 0], # (0, 0) (0, 1) (0, 2) (0, 3) (0, 4)
    [0, 0, 0, 1, 1], # (1, 0) (1, 1) (1, 2) (1, 3) (1, 4)
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0], # (3, 0) (3, 1) (3, 2) (3, 3) (3, 4)
]
freeze_drinks(n, m, ice_shape)
