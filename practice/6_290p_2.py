def get_sum_of_two_numbers(start, end):
    result = 0
    for x in range(start, end + 1):
        result = result + x
    return result

print(get_sum_of_two_numbers(1, 10))
print(get_sum_of_two_numbers(1, 100))
