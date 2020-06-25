balance = 999999
annualInterestRate = 0.18

initialBalance = balance
monthlyInterestRate = annualInterestRate / 12

monthlyPaymentLowerBound = balance / 12
monthlyPaymentUpperBound = balance * (1 + monthlyInterestRate) ** 12 / 12
monthlyPayment = 0

epsilon = 0.01

while abs(balance) > epsilon:
    # Bisection search
    monthlyPaymentMid = \
        (monthlyPaymentLowerBound + monthlyPaymentUpperBound) / 2

    print(f"{monthlyPaymentMid}")

    for month in range(12):
        monthlyUnpaidBalance = balance - monthlyPaymentMid
        monthlyInterest = monthlyInterestRate * monthlyUnpaidBalance

        print(f"Month: {month},", end=' ')
        print(f"Balance: {balance},", end=' ')
        print(f"Minimum Payment: {monthlyPaymentMid},", end=' ')
        print(f"Unpaid Balance: {monthlyUnpaidBalance},", end=' ')
        print(f"Interest: {monthlyInterest}")

        balance = monthlyUnpaidBalance + monthlyInterest

    print(f"BALANCE IS: {balance}")

    if balance > 0 and abs(balance) > epsilon:
        monthlyPaymentLowerBound = monthlyPaymentMid
        balance = initialBalance

    elif balance < 0 and abs(balance) > epsilon:
        monthlyPaymentUpperBound = monthlyPaymentMid
        balance = initialBalance

    else:
        monthlyPayment = round(monthlyPaymentMid, 2)

print(f"Lowest Payment: {monthlyPayment}")
