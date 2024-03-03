before = ["A", "B", "C"]
print("변경 전:", before)

after = []
length = len(before)
for n in range(length):
    idx = length - n - 1
    after.append(before[idx])
print("변경 후:", after)
