list_1 = ["파이썬", "자바", "C언어"]
list_2 = []

for idx in range(len(list_1)):
    temp = [idx, list_1[idx]]
    list_2.append(temp)

print(list_1, ">>>", list_2)


# range 명령어를 사용하지 않는 경우
list_1 = ["파이썬", "자바", "C언어"]
list_2 = []

idx = 0
for value in list_1:
    temp = [idx, value]
    list_2.append(temp)
    idx = idx + 1

print(list_1, ">>>", list_2)
