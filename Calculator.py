# Simple calculator in Python by S. Aniruddh Raam
print("\nCalculator")
a=float(input("Enter Number 1: "))
b=float(input("Enter Number 2: "))
print("\nAdd-->1")
print("Subtract-->2")
print("Multiply-->3")
print("Divide-->4")

# input choice
ch=int(input("\nEnter Choice(1-4): "))

if ch==1:
    c=a+b
    print("Sum = ",c)
elif ch==2:
    c=a-b
    print("Difference = ",c)
elif  ch==3:
    c=a*b
    print("Product = ",c)
elif ch==4:
    if b != 0:
        c=a/b
        print("Quotient = ",c)
    else:
        print("Cannot Divide by Zero!")

else:
    print('Choice invalid')