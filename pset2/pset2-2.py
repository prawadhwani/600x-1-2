balance = 3329
annualInterestRate = 0.2

min_monthly_payment = 0
unpaid_balance = 0
new_balance = 0
while(new_balance != 0):
	unpaid_balance = balance - min_monthly_payment
	#balance due at the beginning of next month
	new_balance = unpaid_balance + (annualInterestRate * unpaid_balance)/12
	min_monthly_payment += 10
print('Lowest Payment: ' + str(min_monthly_payment))