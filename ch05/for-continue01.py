count = range(10)
for n in count:
    if (n + 1) % 3 != 0:
        continue
    print(str(n + 1) + "!")
