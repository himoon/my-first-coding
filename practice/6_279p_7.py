def count_down(number):
    result = []
    for x in range(number):
        result.append(number - x)
    return result

print(count_down(10))
