dict_before = {
    "일요일": "0",
    "월요일": "1",
    "화요일": "2",
    "수요일": "3",
    "목요일": "4",
    "금요일": "5",
    "토요일": "6",
}

keys_before = list(dict_before.keys())
values_before = list(dict_before.values())
length = len(dict_before)
print("keys_before:", keys_before)
print("values_before:", values_before)

dict_after = {}
for n in range(length):
    dict_after[values_before[n]] = keys_before[n]
print(dict_after)
