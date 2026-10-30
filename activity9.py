
r = float(input("Exchange rate: "))
f = float(input("Fee (%): "))
b = float(input("Budget: "))

e = {}
for i in range(3):
    c = input("Category: ")
    a = float(input("Amount: "))
    e[c] = a * r * (1 + f/100)

total = sum(e.values())

print("Total:", total)
print("Largest:", max(e, key=e.get))
print("Status:", "Within Budget" if total <= b else "Over Budget")
