menu = {
    "오늘의 커피": 2800,
    "아메리카노": 3100,
    "카푸치노": 3600,
    "화이트 초콜릿 모카": 4600,
    "플랫 화이트": 4100,
}

my_order = {
    "플랫 화이트": 2,
    "화이트 초콜릿 모카": 1,
}

for x in my_order:
    price = menu[x]
    qty = my_order[x]
    total = price * qty
    print(x + " " + str(qty) + " 잔, 합계 : " + str(total))
