# 주요 라이브러리의 문법과 유의점
# 표준 라이브러리 = 특정한 프로그래밍 언어에서 자주 사용되는 표준 소스코드를 미리 구현해놓은 라이브러리

# 내장함수 - 기본 입출력, 정렬기능 등을 포함하는 기본 내장 라이브러리
# itertools - 반복되는 형태의 데이터를 처리하는 기능을 제공하는 라이브러리, 순열, 조합 라이브러리 제공
# heapq - 힙(Heap) 기능을 제공하는 라이브러리. 우선순위 큐 기능을 구현하기 위해 사용
# bisect - 이진 탐색(Binary Search) 기능을 제공하는 라이브러리
# collections - 덱(deque), 카운터(Counter) 등의 유용한 자료구조를 포함하는 라이브러리

# https://docs.python.org/ko/3/library/index.html

# 내장 함수
result = sum([1,2,3,4,5,6,7,8,9])
print(result)

result = min(4,2,3,4,5,11,1)
print(result)

result = eval("3*7*5") # 문자열로된 수식을 변환후 계산
print(result)

# itertools 
# permutations 
# - 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 일렬로 나열하는 모든 경우(순열) 계산
# - 클래스이므로 객체 초기화 이후에는 리스트 자료형으로 변환해서 사용해야한다
from itertools import permutations
data = ['A', 'B', 'C']
result = list(permutations(data, 3)) # 모든순열(경우) 구함
print(result)

# combinations 
# - 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 순서를 고려하지 않고 나열하는 모든 경우(조합)을 계산
# - 클래스이므로 객체 초기화 이후에는 리스트 자료형으로 변환하여 사용해야 한다
from itertools import combinations
data = ['A', 'B', 'C']
result = list(combinations(data, 2)) # 중복 없음
print(result)

# product
from itertools import product
data = ['A', 'B', 'C']
result = list(product(data, repeat=2)) # 중복 포함
print(result)


# heapq 
# heap 기능을 사용하기 위해 
# 다익스트라 최단 경로 알고리즘 및 당양한 알고리즘에서 우선순위 큐 기능을 구현하고자 할 때 사용
# PriorityQueue 라이브러리도 사용 가능
import heapq

def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8,0])
print(result)