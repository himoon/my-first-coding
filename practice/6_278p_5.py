def square(dataset):
    result = []
    for x in dataset:
        result.append(x * x)
    return result

print(square([3, 2, 5]))
print(square([323, 60]))
