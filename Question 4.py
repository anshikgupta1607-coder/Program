N = input("Enter N: ")
K = int(input("Enter K: "))

length = len(N)

if K > 0:
    # Left rotation
    K = K % length
    result = N[K:] + N[:K]
else:
    # Right rotation
    K = (-K) % length
    result = N[-K:] + N[:-K]

print(result)