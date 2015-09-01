balance = 999999
annualInterestRate = 0.18

min_monthly_payment = 0
unpaid_balance = 0
balanceCopy = balance
monthly_interest_rate = (annualInterestRate)/12.0
#define bounds
low = balance/12
high = (balance *  (1 + monthly_interest_rate)**12)/12.0

lowest_payment = False

while not lowest_payment:
	balance = balanceCopy
	min_monthly_payment = (low + high)/2
	for i in range(12):
		unpaid_balance = balance - min_monthly_payment
		balance = unpaid_balance + (monthly_interest_rate * unpaid_balance)

	if(-0.01 < balance <= 0):
		lowest_payment = True
	elif(balance < 0):
		high = min_monthly_payment
	elif(balance > 0):
		low = min_monthly_payment
	else:
		print('Sorry the balance is off')

print('Lowest Payment: ' + str(round(min_monthly_payment, 2)))