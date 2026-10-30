
u = float(input("Usage: "))
b = float(input("Budget: "))
d = int(input("Validity: "))

plans = [(199, 2, 28), (299, 5, 56), (399, 10, 84)]

best = [(p + max(0, u-g)*50, p) for p,g,v in plans
        if v >= d and p + max(0, u-g)*50 <= b]

if best:
    print("Best Plan:", min(best)[1])
    print("Cost:", min(best)[0])
else:
    print("No Eligible Plan")
