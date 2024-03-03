def trunc(arg, n):
    times = 10**n
    return int(arg * times) / times


print(trunc(0.325, 2))
print(trunc(9.87, 1))
