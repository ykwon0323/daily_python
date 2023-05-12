# 왕실의 나이트 
# 행복 왕국의 왕실 정원은 체스판과 같은 8x8 좌표 정면이다
# 왕실 정원의 특정한 한 칸에 나이트가 서 있다
# 나이트는 매우 충성스러운 신하로서 매일 무술을 연마한다
# 나이트는 말을 타고 있기 때문에 이동을 할 때
# L자 형태로만 이동할 수 있으며
# 정원 밖으로는 나갈 수 없다
# 나이트는 특정한 위치에서 다음과 같은 2가지 경우로 이동할 수 있다
#   1 수평으로 2칸 이동한 뒤에 수직으로 한 칸 이동하기
#   2 수직으로 2칸 이동한 뒤에 수평으로 한 칸 이동하기 
# 나이트가 이동할 수 있는 경우의 수를 출력하는 프로그램 
#   a b c d e f g h
# 1
# 2
# 4
# 5
# 6
# 7
# 8

location = "e5"

location_strs = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8}
x = int(location_strs[location[0]])
y = int(location[1])

move_case = [[-2,-1],[-2,1],[2,-1],[2,1],
             [-1,-2],[-1,2],[1,-2],[1,2]]

result = 0

for move in move_case:
    if move[0]+x < 1 or move[1]+y < 1 or move[0]+x > 8 or move[1]+y > 8:
        pass
    else:
        result += 1
print(result)

# 해설
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]
    # 해당 위치로 이동이 가능하다면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)



