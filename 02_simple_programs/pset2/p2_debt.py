balance = 3329
annualInterestRate = 0.2

initialBalance = balance
monthlyInterestRate = annualInterestRate / 12
guessMonthlyPayment = 10

while balance > 0:
    for month in range(12):
        monthlyUnpaidBalance = balance - guessMonthlyPayment
        monthlyInterest = monthlyInterestRate * monthlyUnpaidBalance

        print(f"Month: {month},", end=' ')
        print(f"Balance: {balance},", end=' ')
        print(f"Minimum Payment: {guessMonthlyPayment},", end=' ')
        print(f"Unpaid Balance: {monthlyUnpaidBalance},", end=' ')
        print(f"Interest: {monthlyInterest}")

        balance = monthlyUnpaidBalance + monthlyInterest

    if balance > 0:
        balance = initialBalance
        guessMonthlyPayment += 10

print(f"Lowest Payment: {guessMonthlyPayment}")
