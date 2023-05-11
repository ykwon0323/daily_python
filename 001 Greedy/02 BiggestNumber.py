# 큰 수의 법칙 
# 다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙이다
# 배열의 특정한 인덱스(번호)에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없다
# 단, 서로 다른 인덱스에 해당하는 수가 같은 경우에도 서로 다른 것으로 간주한다

# 배열의 크기 N (2 <= N <= 1,000) 자연수
# 숫자가 더해지는 횟수 M (1 <= M <= 10,000) 자연수
# 연속가능 횟수 K (1 <= K <= 10,000) 자연수

N = 5
M = 7
K = 2 
nums = [3,4,3,4,3]

result = 0 # 결과
k_cnt = 0 # 연속 카운트

nums.sort()

for _ in range(M):
    if k_cnt >= K:
        result += nums[-2]
        k_cnt = 0
    else:
        result += nums[-1] 
        k_cnt+=1
    
print(result)

# 해설 1 이렇게 하면 시간 초과가 나올수 있음

data = [2, 4, 5, 4, 6]
data = [3,4,3,4,3]

data.sort() # 정렬
first = data[N-1] # 가장 큰 수
second = data[N-2] # 두번째로 큰 수

result = 0 

while True:
    for i in range(K): # 가장 큰 수를 K번 더하기
        if M == 0: # m이 0 이라면 반복문 탈출
            break
        result += first
        M -= 1 # 더할 때마다 1씩 빼기
    if M == 0: # M이 0이라면 반복문 탈출
        break
    result += second # 두번째로 큰 수를 한 번 더하기
    M -= 1 # 더할 때마다 1씩 빼기

print(result)

# 해설 2 반복되는 규칙을 생각
# K+1의 패턴이 M을 벗어나지 않는 사이에 반복될 수 있음

N = 5
M = 7
K = 2 

data = [3,4,3,4,3]

data.sort()

first = data[N-1]
second = data[N-2]

# 가장 큰 수가 등장하는 횟수 
count = int(M / (K + 1)) * K
count += M % (K + 1)

result = 0
result += (count) * first
result += (M - count) * second # 가장 작은 수가 등장하는 횟수

print(result)








