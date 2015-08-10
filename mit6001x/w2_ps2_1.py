balance = 4842
annualInterestRate = 0.2 #annual interest rate as a decimal
monthlyPaymentRate = 0.04 #minimum monthly payment rate as a decimal
tp = 0
mmp = 0
remainb = 0
previusb = balance
unpaidb = balance
interest = 0
for i in range(1,13):
    mmp = monthlyPaymentRate * previusb 
    unpaidb = previusb - mmp
    interest = annualInterestRate/12*unpaidb
    previusb = unpaidb + interest
    tp += mmp
    print 'Month: ', i
    print 'Minimum monthly payment: ', round(mmp, 2)
    print 'Remaining balance: ', round(previusb, 2)
print 'Total paid: ', round(tp,2)
print 'Remaining balance: ', round(previusb, 2)