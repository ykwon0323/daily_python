# 반복문

# while 문
i = 1 
result = 0

while i < 9:
    if i%2 == 1:
        result += i
    i += 1


print(result)

# for 문
for i in range(1, 10):
    print(i)

# for문 안에서 continue 사용 가능
result = list()

for i in range(100):
    if i % 2 == 1:
        result.append(i)
    else:
        continue

print(result)

