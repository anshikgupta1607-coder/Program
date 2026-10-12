balance = float(input("Enter current balance: "))
withdrawal = float(input("Enter withdrawal amount: "))

if withdrawal <= 0:
    print("Invalid Withdrawal Amount")
elif withdrawal > balance:
    print("Insufficient Balance")
else:
    remaining = balance - withdrawal

    print("Withdrawal Successful")
    print("Withdrawn Amount:", withdrawal)
    print("Remaining Balance:", remaining)