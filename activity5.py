
u = float(input("Usage (GB): "))
b = float(input("Budget: "))
d = int(input("Validity days: "))

plans = [(199, 2, 28), (299, 5, 56), (399, 10, 84)]
costs = [p + max(0, u-g)*50 for p, g, v in plans if v >= d and p + max(0, u-g)*50 <= b]

if costs:
    print("Best Plan Cost:", min(costs))
else:
    print("No Eligible Plan")
