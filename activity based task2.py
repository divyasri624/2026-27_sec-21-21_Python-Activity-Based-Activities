#python activity based learning task2.py
months = ["January", "February", "March"]
units = [100, 180, 300]

bills = []

for i in range(len(units)):
    u = units[i]

    if u <= 100:
        bill = u * 2
    elif u <= 200:
        bill = 100 * 2 + (u - 100) * 3
    else:
        bill = 100 * 2 + 100 * 3 + (u - 200) * 5

    bill = bill + 50       # Fixed charge
    bill = bill + bill * 0.05  # 5% surcharge

    bills.append(bill)

    print(months[i], "Units:", u, "Bill: Rs.", round(bill, 2))

    if i > 0 and bills[i] > bills[i - 1] * 1.3:
        print("Warning: Unusual increase in bill!")