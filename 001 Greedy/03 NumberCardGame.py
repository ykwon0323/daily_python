# 숫자 카드 게임
# 여러 개의 숫자 카드 중에서 가장 높은 숫자가 쓰은 카드 한 장을 뽑는 게임
# 1 숫자가 쓰인 카드들이 N X M 형태로 놓여 있다 (N : 행, M : 열)
# 2 먼저 뽑고자 하는 카드가 포함되어 있는 행을 선택
# 3 그다음 선택된 행에 포함된 카드들 중 가장 숫자가 낮은 카드를 뽑아야 함
# 4 따라서 처음에 카드를 골라낼 행을 선택할 때 
#   이후에 해당 행에서 가장 숫자가 낮은 카드를 뽑을 것을 고려하여 
#   최종적으로 가장 높은 숫자의 카드를 뽑을수 있도록 전략을 세워야 함
# 1 <= N, M <= 100
# 1 <= 카드 숫자 <= 10,000 자연수

n = 2
m = 4
cards = [[7, 3, 1, 8],
         [3, 3, 3, 4]]

n = 3
m = 3
cards = [[3, 1, 2],
         [4, 1, 4],
         [2, 2, 2]]

smallest = 1

for arr in cards:
    arr.sort()
    smallest = arr[0] if arr[0] > smallest else smallest
    
print(smallest)

# 해설 1 min() 함수를 이용하는 답안 예시
# n, m = map(int, input().split)

result = 0
# 한 줄씩 입력받아 확인
for i in range(n):
    data = list(map(int, input().split()))
    # 현재 줄에서 가장 작은수 찾기
    min_value = min(data)
    # 가장 작은수들 중에서 가장 큰 수 찾기
    result = max(result, min_value)

print(result)
