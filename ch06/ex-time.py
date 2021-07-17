def convert_seconds(arg):
    if arg < 60:
        # 60초 미만이라면, 초만 출력
        return str(arg) + " 초"

    seconds = arg % 60
    minutes = arg // 60
    if minutes < 60:
        # 60분 미만이라면, 분과 초를 출력
        return str(minutes) + " 분 " + str(seconds) + " 초"

    # 그 외의 경우, 시간, 분, 초를 출력
    hours = minutes // 60
    minutes = minutes % 60
    return str(hours) + " 시간 " + str(minutes) + " 분 " + str(seconds) + " 초 "

print(convert_seconds(3))
print(convert_seconds(60))
print(convert_seconds(323))
print(convert_seconds(60 * 60 + 323 * 2))
