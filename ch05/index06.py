name_set = ["드링킹 요구르트", "딸기 우유", "홈런공"]
price_set = [1800, 1500, 1000]
qty_set = [4, 2, 3]

for i in range(len(name_set)):
    name = name_set[i]
    sales = price_set[i] * qty_set[i]
    print(name + " 매출액 : " + str(sales))
