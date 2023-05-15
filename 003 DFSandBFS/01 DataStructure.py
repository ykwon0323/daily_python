### 꼭 필요한 자료구조 기초
# 탐색 Search 
# 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정

# 자료구조 Data Structure
# 데이터를 표현하고 관리하고 처리하기 위한 구조
#   오버플로 overflow - 가득 찼는데 더 넣으려 하는 경우
#   언더플로 underflow - 비었는데 삭제하려는 경우

### Stack 
# 선입후출 FILO, 후입선출 LIFO

# Stack example
# 삽입 5 - 삽입 2 - 삽입 7 - 삭제 7 - 삭제 - 삽입 1 - 삽입 4 - 삭제
stack = []
stack.append(5)
stack.append(2)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack) # 최하단 원소부터 출력
print(stack[::-1]) # 최상단 원소부터 출력 

### Queue 
# 선입선출 FIFO, 후입후칠 LILO

# Queue example
from collections import deque

# 큐(Queue) 구현을 위한 deque 라이브러리 사용
queue = deque()

# 삽입 5 - 삽입 2 - 삽입 7 - 삭제 7 - 삭제 - 삽입 1 - 삽입 4 - 삭제
queue.append(5)
queue.append(2)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue) # 먼저 들어온 순서대로 출력
queue.reverse() # 다음 출력을 위해 역순으로 바꾸기
print(queue)

# deque 라이브러리
# stack 장점 + que 장점 
# 데이터를 넣고 빼는 속도가 리스트 자료형에 비해 효율적
# queue 라이브러리 이용하는 것보다 간단

### 재귀함수 Recursive Function 
# example
def recursive_function():
    print('재귀함수를 호출합니다')
    recursive_function()

# recursive_function() # 파이썬에는 횟수 제한이 존재한다 그래서 오류가 나며 종료된다

# 재귀함수 종료조건 condition for off the recursive Function
# example
def recursive_function(i):
    # 100번째 출력했을 때 종료되도록 종료 조건 명시
    if i == 100:
        return
    print(i, '번째 재귀함수에서', i+1,'번째 재귀 함수를 호출합니다')
    recursive_function(i+1)
    print(i, '번째 재귀 함수를 종료합니다')

recursive_function(1) # Recursive == Stack

### 반복적(literative) <->  재귀적(Recursive) 대비되는 의미로 사용된다
# 팩토리얼(!) 예재
# 반복적으로 구현한 n!
def factorial_iterative(n):
    result = 1
    # 1부터 n까지의 수를 차례대로 곱하기
    for i in range(1, n+1):
        result *= i
    return result

# 재귀적으로 구현한 n!
def factorial_recursive(n):
    if n <= 1: # n이 1 이하인 경우 1을 반환
        return 1
    # n! = n * (n-1)을 그대로 코드로 작성하기
    return n * factorial_recursive(n-1)

print('반복적으로 구현', factorial_iterative(5))
print('재귀적으로 구현', factorial_recursive(5))

# 반복문 대신 재귀 함수를 사용할 때에 이점?
# 코드가 간결해진다 
# 재귀 함수가 수학의 점화식(재귀식)이기 때문이다
# 점화식? - 특정한 함수를 자신보다 더 작은 변수에 대한 함수와의 관계로 표현한 것을 의미

