def print_reverse_hashes(rows):
    for x in range(rows):
        count = x + 1
        print(" " * (rows - count) + "#" * count)

print_reverse_hashes(4)
