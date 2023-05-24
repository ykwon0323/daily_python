# 두 배열의 원소 교체
# 두 개의 배열 A, B
# N개의 원소로 구성, 자연수
# 최대 K번의 바꿔치기 연산을 수행 가능
# 배열 A에 있는 원소 하나 <=> 배열 B에 있는 원소 하나 (교체)
# 목표 : 배열 A의 모든 원소의 합이 최대가 되도록 하는 것
# 1 <= N <= 100000
# 0 <= K <= N 

n = 5
k = 3
arr_a = [1, 2, 5, 4, 3]
arr_b = [5, 5, 6, 6, 5]

for i in range(k):
    arr_a.sort()
    arr_b.sort(reverse=True)
    arr_a[0], arr_b[0] = arr_b[0], arr_a[0]

print(sum(arr_a))

