def get_length(arg):
    cnt = 0
    for _ in arg:
        cnt = cnt + 1
    return cnt


print(get_length("python"))
print(get_length([3.23]))
print(get_length({1: 1, 2: 2, 3: 3}))
