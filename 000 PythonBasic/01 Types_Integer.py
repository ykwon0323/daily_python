# 정수형 Integer
a = 1000 # 양의 정수
print(a)

a = -7 # 음의 정수
print(a)

# 0
a = 0
print(a)

# 실수형 Real Number
# 양의 실수
a = 123.44
print(a)

# 음의 실수 0 생략가능
a = - 123.
print(a)

# 지수 표현
# 10억 지수 표현
a = 1e9
print(a)

# 152.5
a = 15.25e1
print(a)

# 3.33
a = 333e-2
print(a)

# 컴퓨터는 실수를 정확하게 표현하지 못한다
a = 0.3 + 0.6
print(a)

if a == 0.9:
    print(True)
else:
    print(False)

# round 함수 사용 
a = 0.3 + 0.6
print(round(a, 7))

# 수 자료형 연산
a = 7
b = 3

# 나누기 /
print(a/b)
# 나머지 %
print(a%b)
# 몫 //
print(a//b)

# 거듭제곱 **
print(2 ** 3)

