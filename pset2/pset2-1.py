#initialize minimum pay and total paid
min_monthly_payment = 0
total_paid = 0
#loop through 12 months
for i in range (1,13):
	print('Month: ' + str(i))
	#find the min pay
	min_monthly_payment = round((balance * monthlyPaymentRate),2)
	print('Minimum monthly payment: '+ str(min_monthly_payment))
	#remaining balance
	unpaid_balance = balance - min_monthly_payment
	#calculate interest on it
	balance = round(unpaid_balance + (annualInterestRate * unpaid_balance)/12, 2)
	print('Remaining balance: ' + str(balance))
	total_paid += min_monthly_payment
	
print('Total Paid: ' + str(total_paid))
print('Remaining balance: '+ str(balance))