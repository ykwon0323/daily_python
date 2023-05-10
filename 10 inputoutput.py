# 입출력

# 입력을 위한 전형적인 소스코드 
# n = int(input())

# # 각 데이터를 공백으로 구분하여 입력 
# data = list(map(int, input().split()))

# data.sort(reverse = True)
# print(data)

# sys.stdin.readline() input()함수가 느리기 때문에 사용
import sys
data = sys.stdin.readline().rstrip()
print(data)
