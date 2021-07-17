def get_sum_and_average(arg):
    length = len(arg)
    if length == 0:
        return "[오류] 요소의 개수가 0 입니다"

    total = 0
    for x in arg:
        total = total + x
    return {"합계": total, "평균": total / length}

print(get_sum_and_average([]))
print(get_sum_and_average([3, 2]))
print(get_sum_and_average([-1, 0, 1, 2, 3]))
