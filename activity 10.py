
v = float(input("Venue: "))
e = float(input("Equipment: "))
c = float(input("Catering: "))
t = float(input("Transport: "))
ce = float(input("Certificates: "))
s = float(input("Sponsorship: "))
p = float(input("Participant fee: "))

total = v + e + c + t + ce
short = max(0, total - s)

print("Total Cost:", total)
print("Shortfall:", short)
print("Minimum Registrations:", int(short/p) + (short % p > 0))
