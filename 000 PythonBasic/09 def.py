# 함수
# def 함수명(매개변수):
#     실행코드
#     return 변환값

def add(a, b):
    print(a + b)


# 호출방법 1 
add(5, 7)
# 호출방법 2 매개변수 지정
add(a = 8, b = 10)

# 함수 안에서 함수 밖에 변수를 변경 할 경우 global 키워드 이용 
a = 0
def func():
    global a
    a += 1

for i in range(10):
    func()

print(a)

# normal
def add(a, b):
    return a + b

# lamda
(lambda a, b: a+b)(8, 7)

print((lambda b, c: b*c)(7, 8))
    




