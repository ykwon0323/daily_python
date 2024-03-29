# 미로 탈출
# N X M 미로
# 시작 (1, 1)
# 출구 (N, M)
# 괴물 있음 0 / 없음 1
# 탈출을 위한 최소 칸의 개수
# 시작 칸, 마지막 칸을 모두 포함해서 계산

# 4 <= N, M <= 200

# n = 5
# m = 6

# map = [[1, 0, 1, 0, 1, 0],
#        [1, 1, 1, 1, 1, 1],
#        [0, 0, 0, 0, 0, 1],
#        [1, 1, 1, 1, 1, 1],
#        [1, 1, 1, 1, 1, 1]]

# 해설 
from collections import deque

# N, M을 공백으로 구분하여 입력받기
# n, m = map(int, input().split())

n = 5
m = 6
# 2차원 리스트의 맵 정보 입력받기
# graph = []
# for i in range(n):
#     graph.append(list(map(int, input())))

graph = [[1, 0, 1, 0, 1, 0],
         [1, 1, 1, 1, 1, 1],
         [0, 0, 0, 0, 0, 1],
         [1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1]]

# 이동할 네 방향 정의(상, 하, 좌, 우) 
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 소스코드 구현
def bfs(x, y):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x, y))
    print(queue)
    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 네 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로찾기 공간을 벗어난 경우 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            # 벽인 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    # 가장 오른쪽 아래까지 최단 거리 반환
    print(graph)
    return graph[n-1][m-1]

# BFS를 수행한 결과 출력
print(bfs(0, 0))

[[3, 0, 5, 0, 7, 0], 
 [2, 3, 4, 5, 6, 7], 
 [0, 0, 0, 0, 0, 8], 
 [14, 13, 12, 11, 10, 9], 
 [15, 14, 13, 12, 11, 10]]

graph = [[1, 0, 1, 0, 1, 0],
         [1, 1, 1, 1, 1, 1],
         [0, 0, 0, 0, 0, 1],
         [1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1]]

