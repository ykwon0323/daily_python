# Greedy 
# 현재 상황에서 가장 좋은 것만 고르는 방법

# 거스름돈
# 거슬러 줘야할 돈이 N원일 때, 거슬러 줘야 할 동전의 최소 개수를 구하라
# 500원, 100원, 50원, 10원 동전 무한히 사용 가능
import time

start_time = time.time()
target = 1340 # 500(2)/ 100(3)/ 10(4)
coins = 0

def checking():
    global target
    if target == 0:
        print(coins)


coins += target//500
target -= (target//500)*500
checking()

coins += target//100
target -= (target//100)*100
checking()

coins += target//50
target -= (target//50)*50
checking()

coins += target//10
target -= (target//10)*10
checking()

end_time = time.time()

print("time :", end_time - start_time )

# 해설

start_time_2 = time.time()
n = 1340
count = 0

coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n // coin
    n %= coin

print(count)

end_time_2 = time.time()

print("time :", end_time_2 - start_time_2 )

# [주의]의심 해 볼 것, 이 경우는 큰 동전이 작은 동전들의 배수 이므로 정당하다 
# 아닌 경우 예시,
#   동전의 종류가 (500, 400, 100)이런경우 800원을 거슬러 주려고 할 때
#   현재 알고리즘으로는 500, 100, 100, 100 이 나오게 된다
#   하지만 정답은 400, 400이 맞다
#    