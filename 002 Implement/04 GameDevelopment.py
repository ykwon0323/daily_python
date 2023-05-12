# 게임 개발 
# 현민이는 게임 캐릭터가 맵 안에서 움직이는 시스템을 개발 중이다
# 캐릭터가 있는 장소는 1x1 크기의 정사각형으로 이뤄진 NxM 크기의 직사각형으로, 각각의 칸은 육지 또는 바다이다
# 캐릭터는 동서남북 중 한 곳을 바라본다
# 맵의 각 칸은 (A, B)로 나타낼 수 있고
# A는 북쪽으로부터 떨어진 칸의 개수
# B는 서쪽으로부터 떨어진 칸의 개수이다
# 캐릭터는 상하좌우로 움직일 수 있고
# 바다로 되어 있는 공간에는 갈 수 없다
# 캐릭터의 움직임을 설정하기 위해 정해 놓은 메뉴얼
#   1 현재 위치에서 현재 방향을 기준으로 왼쪽 방향(반시계 방향으로 90도 회전한 방향)부터 차례대로 갈 곳을 정한다
#   2 캐릭터의 바로 왼쪽 방향에 아직 가보지 않은 칸이 존재한다면, 왼쪽 방향으로 회전한 다음 왼쪽으로 한칸을 전진한다
#       왼쪽 방향에 가보지 않은 칸이 없다면, 왼쪽 방향으로 회전만 수행하고 1단계로 돌아간다
#   3 만약 네 방향 모두 이미 가본 칸이거나 바다로 되어 있는 칸인 경우에는, 
#       바라보는 방향을 유지한 채로 한 칸 뒤로 가고 1단계로 돌아간다
#       단, 이때 뒤쪽 방향이 바다인 칸이라 뒤로 갈 수 없는 경우에는 움직임을 멈춘다

# 세로크기 N 3 <= N <= 50
# 가로크기 M 3 <= M <= 50
# 0: 북 / 1: 동 / 2: 남 / 3: 서 
# 0: 육지 / 1: 바다
# 방문한 칸의 수 출력

n = 4
m = 4
x = 1
y = 1
look = 0 
game_map = [[1, 1, 1, 1],
            [1, 0, 0, 1],
            [1, 1, 0, 1],
            [1, 1, 1, 1]]

map_history = [[0, 0, 0, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 0]]

look_list = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# 1 현재 위치에서 현재 방향을 기준으로 왼쪽 방향(반시계 방향으로 90도 회전한 방향)부터 차례대로 갈 곳을 정한다
#   2 캐릭터의 바로 왼쪽 방향에 아직 가보지 않은 칸이 존재한다면, 왼쪽 방향으로 회전한 다음 왼쪽으로 한칸을 전진한다
#       왼쪽 방향에 가보지 않은 칸이 없다면, 왼쪽 방향으로 회전만 수행하고 1단계로 돌아간다
#   3 만약 네 방향 모두 이미 가본 칸이거나 바다로 되어 있는 칸인 경우에는, 
#       바라보는 방향을 유지한 채로 한 칸 뒤로 가고 1단계로 돌아간다
#       단, 이때 뒤쪽 방향이 바다인 칸이라 뒤로 갈 수 없는 경우에는 움직임을 멈춘다
turn_cnt = 0
result = 1

map_history[x][y] = 1

while True:
    
    print('x :',x,'y :',y)
    # 1 방향 정하기
    look = look-1 if look > 0 else 3
    turn_cnt += 1
    # 이동할 곳
    px = x + look_list[look][0]
    py = y + look_list[look][1]
    # 2 방문 확인
    if map_history[px][py] == 0 and game_map[px][py] == 0:
        # 이동
        x = px
        y = py
        turn_cnt = 0
        # 기록
        map_history[px][py] = 1
        result += 1
    # 3 이동불가
    if turn_cnt > 3:
        bx = x + look_list[look][0]*-1
        by = y + look_list[look][1]*-1
        if game_map[px][py] == 1:
            break
        else:
            x = bx
            y = by
            
print('x :',x,'y :',y)
print(result)

print('------------')
# 해설 - 나는 최초 위치를 히스토리에 기록해놓는 과정을 빼먹어서 과정이 틀리게 나왔었다
# n. m = map(int, input().split())
n = 4
m = 4

# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
d = [[0] * m for _ in range(n)]

# 현재 캐릭터의 X 좌표, Y 좌표, 방향
x = 1
y = 1
direction = 0
d[x][y] = 1 # 현재 좌표 방문 처리 [내가 틀린 부분]

# 전체 맵 정보
array = [[1, 1, 1, 1],
        [1, 0, 0, 1],
        [1, 1, 0, 1],
        [1, 1, 1, 1]]

# 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# 시뮬레이션 시작
count = 1
turn_time = 0
while True:
    print('x :',x,'y :',y)
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있다면 이동하기
        if array[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤가 바다로 막혀있는 경우
        else:
            break
        turn_time = 0
# 정답 출력

print('x :',x,'y :',y)
print(count)


