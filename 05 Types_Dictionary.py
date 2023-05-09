# 사전 자료형
# - key : 변경 불가능한 데이터
# - value 

data = dict()
data['a'] = 'apple'
data['b'] = 'banana'
data['c'] = 'car'

print(data)

# keys() => 키 데이터만 뽑아서 리스트로 
keys = data.keys()
# values() => 값 데이터만 뽑아서 리스트로
values = data.values()

print(keys)
print(values)