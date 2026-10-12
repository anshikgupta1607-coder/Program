a = int(input("Enter first positive integer: "))
b = int(input("Enter second positive integer: "))

LHS = (a + b) ** 3
RHS = a ** 3 + b ** 3 + 3 * a ** 2 * b + 3 * a * b ** 2

print("LHS =", LHS)
print("RHS =", RHS)

if LHS == RHS:
    print("VERIFIED")
else:
    print("NOT VERIFIED")