opening = 54700
closing = 55700
diff = closing - opening
if diff > 0:
    print("↑" + str(diff))
elif diff < 0:
    print("↓" + str(abs(diff)))
else:
    print("-")
