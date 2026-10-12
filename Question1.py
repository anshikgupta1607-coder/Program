units=int(input("Enter the number of units electricity consumed"))
if units<=100:
    rate=5
elif units <= 200:
    rate=7
elif units <= 300:
    rate=10
else:
    rate=12

bill= units * rate

print("Electricity Bill:",bill)
            