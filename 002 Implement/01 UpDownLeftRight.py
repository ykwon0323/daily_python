# 구현 문제
# 완전 탬색 - 모든 경우의 수를 주저 없이 다 계산하는 해결 방법
# 시뮬레이션 - 문제에서 제시한 알고리즘을 한 단계씩 차례대로 직접 수행

# 상하좌우 문제
# 여행가 A는 N X N 크기의 정사각형 공간 위에 서 있다
# 이 공간은 1x1 크기의 정사각형으로 나누어져 있다
# 가장 왼쪽 위 좌표는 (1, 1)이며, 가장 오른쪽 아래 좌표는 (N, N)에 해당한다
# 여행가 A는 상, 하, 좌, 우 방향으로 이동할 수 있으며, 시작 좌표는 항상 (1, 1)이다
# 여행 계획서에는 하나의 줄에 띄어쓰기를 기준으로 하여 
# L, R, U, D 중 하나의 문자가 반복적으로 적혀 있다
# L - 왼쪽 한칸 이동
# R - 오른쪽 한칸 이동
# U - 위쪽 한칸 이동
# D - 아래쪽 한칸 이동
# N X N 크기의 정사각형 공간을 벗어나는 움직임은 무시된다

# 1 <= N <= 100
# 1 <= 이동횟수 <= 100 
# 최종적으로 도착할 지점의 좌표 (X,Y) 출력

n = 5
plans = ["R", "R", "R", "R", "R", "R", "U", "D", "D"]

x = 1
y = 1

loopCnt = 0

for move in plans:
    loopCnt += 1
    if move == "L" and y > 1: # 좌 y-1
        y -= 1
    elif move == "R" and y < n: # 우 y+1
        y += 1
    elif move == "U" and x > 1: # 상 x-1
        x -= 1
    elif move == "D" and x < n: # 하 x+1
        x += 1
    else:
        pass

print(x, y ,'/', loopCnt)

# 해설 시뮬레이션 유형으로 분류되는 문제 

n = 5
plans = ["R", "R", "R", "R", "R", "R", "U", "D", "D"]
x = 1
y = 1

# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

loopCnt = 0
# 이동 계획을 하나씩 확인
for plan in plans:
    loopCnt += 1
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        loopCnt += 1
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    # 이동 수행
    x, y = nx, ny

print(x, y ,'/', loopCnt)
