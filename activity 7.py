
n = int(input("Products: "))
total = 0

for i in range(n):
    name = input("Product: ")
    p = float(input("Price: "))
    q = int(input("Quantity: "))
    c = input("Category (food/other): ")

    amt = p * q
    tax = amt * (5 if c == "food" else 12) / 100
    total += amt + tax

discount = min(total * 0.10, 500) if total >= 2000 else 0

print("Total:", total)
print("Discount:", discount)
print("Final Bill:", total - discount)
