balance = 4773
annualInterestRate = 0.2

min_monthly_payment = 0
unpaid_balance = 0
balanceCopy = balance

while balance > 0:
	balance = balanceCopy
	min_monthly_payment += 10
	for i in range(12):
		unpaid_balance = balance - min_monthly_payment
		balance = unpaid_balance + (annualInterestRate * unpaid_balance)/12

print('Lowest Payment: ' + str(min_monthly_payment))

#how could we write code that would reset the balance to the initial balance, increase the payment by $10, and try again

#how the program will know when it has found a good minimum monthly payment value

#you don't want to overwrite the original value of balance