#Write a program to enter P, T, R and calculate Compound Interest.

p = float(input("Enter Principal amount: "))
t = float(input("Enter Time: "))
r = float(input("Enter Rate of interest: "))

amount = p * (1 + r / 100) ** t
ci = amount - p

print("Compound Interest =", ci)
print("Amount =", amount)