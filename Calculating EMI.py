#Python program to calculate monthly EMI (Equated Monthly Installment)
#EMI Formula = p * r * (1+r)^n/((1+r)^n-1)
#If the interest rate per annum is R% then
#interest rate per month is calculated using:
#Monthly Interest R-ate (r) = R/(12*100)
#Varaible name details:
#p = Principal or Loan Amount
#r = Interest Rate Per Month
#n = Number of monthly installments
#Reading inputs from user
p = float(input("Enter principal amount: "))
r = float(input("Enter annual interest rate: "))
n = int(input("Enter number of months: " ))
# Calculating Equated Monthly Installment (EMI)
emi = p * r * ((1+r)**n)/((1+r)**n - 1)
print("Monthly EMI = ", emi)
