count = range(20)
for x in count:
    if ((x + 1) % 10) != 0:
        continue
    print(str(x + 1) + "!")
