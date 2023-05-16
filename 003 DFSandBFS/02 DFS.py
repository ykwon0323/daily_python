# DFS 
# Depth-First Search 
# 깊이 우선 탐색, 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘
# Graph - Node(Vertex) - Edge
# 재귀함수 이용

# 인접 행렬 Adjacency Matrix : 2차원 배열로 그래프의 연결 관계를 표현하는 방식
# - 2차원 배열에 각 노드가 연결된 형태를 기록하는 방식
# 예제
INF = 999999999 # 무한의 비용 선언
# 2차원 리스트를 이용해 인접 행렬 표현
graph = [
    [0, 7, 5],
    [7, 0, INF],
    [5, INF, 0]
]

print(graph)
# 인접 리스트 Adjacency List : 리스트로 그래프의 연결 관계를 표현하는 방식
# 예제
# 행(Row)이 3개인 2차원 리스트로 인접 리스트 표현
graph = [[] for _ in range(3)]

# 노드 0에 연결된 노드 정보 저장(노드, 거리)
graph[0].append((1,7))
graph[0].append((2,5))

# 노드 1에 연결된 노드 정보 저장(노드, 거리)
graph[1].append((0,7))

# 노드 2에 연결된 노드 정보 저장(노드, 거리)
graph[2].append((0,5))

print(graph)

# 특정한 노드와 연결된 모든 인접 노드를 순회해야 하는 경우,
# 인접 리스트 방식이 인접 행렬 방식에 비해 메모리 공간의 낭비가 적다

# DFS 예제

# DFS 메서드 정의
def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
    
# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]
# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False]*9

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)