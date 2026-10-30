
m = float(input("Material cost: "))
l = float(input("Labour cost: "))
w = float(input("Wastage cost: "))
mc = float(input("Machine cost: "))
s = float(input("Selling price: "))
t = float(input("Profit target: "))

cost = m + l + w + mc
profit = s - cost

print("Total Cost:", cost)
print("Profit:", profit)
print("Result:", "Achieved" if profit >= t else "Not Achieved")
