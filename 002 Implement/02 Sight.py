# 시각
# 정수 N이 입력되면 00h00m00s ~ Nh59mh59s 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 구해라
# 0 <= N <= 23

n = 5 

result = 0
loopCnt = 0
for h in range(n+1):
    loopCnt += 1
    if "3" in str(h):
         result += 3600
    else:
        for m in range(60):
            loopCnt += 1
            if "3" in str(m):
                result += 60
            else:
                for s in range(60):
                   loopCnt += 1
                   if "3" in str(s):
                        result += 1
print(result, loopCnt)

# 해설 - 완전탐색 유형 확인(탐색)해야 할 전체 데이터의 개수가 100만개 이하일 때 완전 탐색을 사용하면 적절
n = 5 
result = 0
loopCnt = 0 
for h in range(n+1):
    loopCnt += 1
    for m in range(60):
        loopCnt += 1
        for s in range(60):
            loopCnt += 1
            if "3" in (str(h)+str(m)+str(s)):
                result += 1
print(result, loopCnt)

# for문의 이해가 좀 부족한듯 ㅠ

arr = [i for i in range(10)]
print(arr)

arr = [i for i in range(9)]
print(arr)

arr = [i for i in range(0, 9)]
print(arr)