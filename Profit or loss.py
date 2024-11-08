
actual_cost = float(input(" Please Enter the Actual Product Price: "))
sale_amount = float(input(" Please Enter the Sales Amount: "))
if(actual_cost - sale_amount > 0):
    amount = actual_cost - sale_amount
    print("Total Loss Amount = ",amount)
elif(sale_amount - actual_cost > 0):
    amount = sale_amount - actual_cost
    print("Total Profit = ",amount)
else:
    print("No Profit No Loss!!!")
input()
