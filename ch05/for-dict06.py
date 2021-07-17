mos_qty = {
    "2020년6월": [9, 5, 14, 8],
    "2020년7월": [15, 6, 17, 15],
    "2020년8월": [26, 18, 26, 10]
}

for month in mos_qty:
    total = sum(mos_qty[month])
    print(month + " 판매량 : " + str(total))
