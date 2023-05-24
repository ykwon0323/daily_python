# 계수 정렬 Count Sort
# 특정한 조건이 부합할 때만 사용할 수 있지만 매우 빠른 정렬 알고리즘
# '데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때'
# 무한한 범위를 가질 수 있는 실수형 데이터가 주어지는 경우 계수 정렬은 사용하기 어려움
# 데이터 차이 백만을 넘지 않을 때 효과적임
# 모든 범위를 담을 수 있는 크기의 리스트(배열)을 선언 해야 하기 때문
# 비교 기반의 정렬 알고리즘과는 다름

# example 
# 모든 원소의 값이 0보다 크거나 같다고 가정
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
# 모든 범위를 포함하는 리스트 선언(모든 값은 0으로 초기화)
count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1 # 각 데이터에 해당하는 인덱스의 값 증가

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')

# 데이터 범위만 한정되어 있다면 효과적으로 사용할 수 있으며 항상 빠르게 동작함
# 기수 정렬 Radix Sort 과 더불어서 가장 빠르다고 볼 수있음
# 하지만 공간 복잡도가 높은편이라 메모리가 제약이 걸릴 경우가 높음
