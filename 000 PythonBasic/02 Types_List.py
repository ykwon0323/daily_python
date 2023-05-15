# 리스트 
# - [] 안에 넣어서 초기화
# - , 쉼표로 구분
# - 접근 리스트[인덱스]
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)
print(a[2])

# 빈 리스트 선언 방법
b = list()
print(b)
c = []
print(c)

# 특정 원소에 접근하는 것 = indexing 
# - 양의 정수 인덱스, 앞에서부터 탐색
# - 음의 정수 인덱스, 뒤에서부터 탐색
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(a[-1])

# 값 변경
a[1] = 3
print(a)

# 연속적인 위치에 값들 접근 = slicing
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a[2:4]) # 3,4

# 리스트 초기화 = 리스트 컴프리헨션

# 0부터 20까지 홀수만 포함하는 리스트
array = [i for i in range(20) if i%2 == 1]

print(array)

# 1부터 9까지의 수의 제곱 값을 포함하는 리스트
array = [i * i for i in range(1, 10)]
print(array)

# N x M 크기의 2차원 리스트 초기화
n = 3
m = 4 
array = [[0]* m for _ in range(n)]
print(array)

# 파이썬에서 _ 언더바 
# - 반복을 위한 변수의 값을 무시하고자 할 때 
summary = 0 
for i in range(1, 10):
    summary += i
print(summary)

for _ in range(5):
    print("hello")

array = [[0,2,3,4] for _ in range(3)]
print(array)

# 리스트 관련 메서드
# append 마지막에 하나 추가 
# sort 기본정렬 오름차순
# sort(reverse=True) 내림차순
# insert(삽입위치) 값 삽입
# count(특정값) 특정값 개수 카운트
# remove(특정값) 특정값 원소를 제거, 여러개면 하나만 제거
a = [1, 4, 3]
print('기본리스트', a)

a.append(2)
print('append', a)

a.sort()
print('sort', a)

a.sort(reverse=True)
print('sort(reverse=True)', a)

a.insert(1, 99)
a.insert(3, 99)
a.insert(-1, 2)
print('insert', a)

cnt = a.count(2)
print(cnt)

a.remove(99)

for _ in range(cnt):
    a.remove(2)

print(a)


# 특정값을 포함하지 않게끔 리스트 조정하기
a = [1, 2, 3, 4, 5, 5, 5]
remove_set = [3, 5]

result = [ i for i in a if i not in remove_set]

print(result)



