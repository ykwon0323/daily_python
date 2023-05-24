# 선택 정렬 Selection Sort
# 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸고
# 그 다음 작은 데이터를 선택해 앞에서 두번째 데이터와 바꾸는 과정을 반복
# "매번 가장 작은것을 선택한다"

# example
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i # 가장 작은 원소의 인덱스
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i] # 스와이프

print(array)

# 비효율적임