balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

monthlyInterestRate = annualInterestRate / 12

for month in range(12):
    minMonthlyPayment = monthlyPaymentRate * balance
    monthlyUnpaidBalance = balance - minMonthlyPayment
    monthlyInterest = monthlyInterestRate * monthlyUnpaidBalance

    print(f"Month: {month},", end=' ')
    print(f"Balance: {balance},", end=' ')
    print(f"Minimum Payment: {minMonthlyPayment},", end=' ')
    print(f"Unpaid Balance: {monthlyUnpaidBalance},", end=' ')
    print(f"Interest: {monthlyInterest}")

    balance = monthlyUnpaidBalance + monthlyInterest

print(f"Remaining balance: {round(balance, 2)}")
