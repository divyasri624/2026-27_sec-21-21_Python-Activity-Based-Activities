
name = input("Enter patient name: ")
c = float(input("Consultation charges: "))
d = float(input("Diagnostic charges: "))
t = float(input("Treatment charges: "))
p = input("Patient type (Senior/Regular): ")

if c < 0 or d < 0 or t < 0:
    print("Invalid Charges")
else:
    total = c + d + t
    discount = total * 0.10 if p.lower() == "senior" else 0
    bill = total - discount

    print("Patient:", name)
    print("Total:", total)
    print("Discount:", discount)
    print("Final Bill:", bill)

    if bill >= 10000:
        print("High Payment")
    elif bill >= 5000:
        print("Medium Payment")
    else:
        print("Low Payment")
