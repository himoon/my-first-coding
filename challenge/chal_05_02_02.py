list_key = ["종목", "날짜", "종가"]
list_value = ["엔비디아", "2024-02-26", 790.92]

dict_price = {}
for idx in range(len(list_key)):
    key = list_key[idx]
    value = list_value[idx]
    dict_price[key] = value

print("list_key >>>", list_key)
print("list_value >>>", list_value)
print("dict_price >>>", dict_price)
