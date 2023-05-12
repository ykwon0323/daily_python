# 1이 될 때까지
# 어떠한 수 N이 1이 될 때까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행하려고 한다
# 단, 두번째 연산은 N이 K로 나누어 떨어질 때만 선택할 수 있다
#   1 N에서 1을 뺀다
#   2 N을 K로 나눈다
# 2 <= N <= 100,000
# 2 <= K <= 100,000
# N >= K

n = 25
k = 5 

n = 17
k = 4
result = 0

while True:
    if n == 1:
        break
    if n % k == 0:
        n /= k
    else:
        n -= 1
    result +=1

print(result)