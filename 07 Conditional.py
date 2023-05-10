# 조건문 

x = 15 
if x >= 10:
    print(x)

x = 2
if x < 1 :
    print("x는 1보다 작습니다")
elif x > 3 :
    print("x는 3보다 큽니다")
else:
    print("x는 2입니다")

# 논리연산자
x = 1
y = 2

print(x == 1 and y == 2)
print(x == 1 and y == 3)
print(x == 1 or y == 3)
print(not (x == 1 or y == 3))

# in 연산자와 not in 연산자
array = [1,2,3,4,5,6,7,8,9]

print(5 in array)
print(789 not in array)

str = "hello"

print('h' in str)

# pass 사용 가능

b = 1

if b == 1:
    pass
elif b == 2:
    print("b가 2임")
else:
    print("아무것도 아니다")

# 한 줄 표현 가능 if결과/if조건/else/else결과
score = 85

result = "Success" if score > 85 else "Fail"

print(result)

# 수학과 동일한 표현식 사용 가능 

m = 2

print(1 < m < 3)

print(1 < m and m< 3)