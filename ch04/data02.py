yo_price = 1800
yo_qty = 4
milk_price = 1500
milk_qty = 2
hr_price = 1000
hr_qty = 3

yo_sales = yo_price * yo_qty
milk_sales = milk_price * milk_qty
hr_sales = hr_price * hr_qty

total_sales = yo_sales + milk_sales + hr_sales
total_qty = yo_qty + milk_qty + hr_qty

print("드링킹 요구르트 매출액 : " + str(yo_sales))
print("딸기 우유 매출액 : " + str(milk_sales))
print("홈런공 매출액 : " + str(hr_sales))
print("-" * 20)
print("총매출액 : " + str(total_sales))
print("총판매량 : " + str(total_qty))
