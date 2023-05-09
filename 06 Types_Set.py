# 집합 자료형
# - 중복을 허용하지 않는다
# - 순서가 없다
# {}로 사용

data = set([1, 1, 2, 3, 4, 4, 5])
print(data)

data = {1, 1, 1, 1}
print(data)

a = set([1, 2, 3, 4, 5])
b = set([3, 4, 5, 6, 7])

print(a | b) # 합집합
print(a & b) # 교집합
print(a - b) # 차집합
print(b - a) # 차집합

# 메서드 add, update, remove
data = set([1,2,3,4,5,6,7,8])
# add 하나만 추가할 경우
data.add(77)
print(data)
# update 여러개 추가할 경우
data.update([66,33,123456])
print(data)
# remove 특정 원소 삭제
data.remove(123456)
print(data)
