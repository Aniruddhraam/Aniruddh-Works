#7
age=int(input("TYPE YOUR AGE"))
n=age+10
print("IN TEN YEARS YOU WILL BE",n,"YEARS OLD")

#8
li=float(input("ENTER LIABILITIES"))
ca=float(input("CAPITAL"))
asse=li+ca
print(asse)

#9
STdeb=float(input("ENTER SHORT TERM DEBT"))
LTdeb=float(input("ENTER LONG TERM DEBT"))
TA=float(input("ENTER TOTAL ASSETS"))
ans=STdeb+LTdeb/TA
print(ans)

#10
import math
a = float(input("Enter base: "))
b = float(input("Enter height: "))
x = float(input("Enter angle: "))
c = math.sqrt(a ** 2 + b ** 2)
print("Hypotenuse =", c)

#11
import math
a=float(input("ENTER AREA"))
r=math.sqrt(a*7/88)
print("RADIUS=",r)

#12
w=(input("ENTER A WORD"))
l=len(w)
print("eka"*l)

#13
import math
r=float(input("ENTER RADIUS"))
vol=4/3*math.pi*r**2
print(vol)

#16
CP=float(input("ENTER CP"))
pp=float(input("ENTER PROFIT IN PERCENTAGE"))
p=CP*pp/100
print(CP-p)

#17
basic=float(input("ENTER BASIC SALARY"))
hp=float(input("ENTER HRA IN PERCENTAGE"))
dp=float(input("ENTER DP IN PERCENTAGE"))
tp=float(input("ENTER TAX IN PERCENTAGE"))
hra=basic*hp/100
da=dp*basic/100
tax=tp*basic/100
net=basic+hra+da-tax
print(net)

#18
print("Calculator by Aniruddh Raam")
print("Addition-->1")
print("Subtraction-->2")
print("Multiplication-->3")
print("Division-->4")
ch=int(input("Enter you choice"))
if ch==1:
    a=int(input("Enter value 1"))
    b=int(input("Enter value 2"))
    z=a+b
    print("Answer= ",z)

if ch==2:
    a=int(input("Enter value 1"))
    b=int(input("Enter value 2"))
    ans=a-b
    print("Answer = ",ans)
if ch==3:
    a=int(input("Enter value 1"))
    b-int(input("Enter value 2"))
    ans=a*b
    print("Answer = ",ans)
if ch==4:
    a=int(input("Enter Dividend"))
    b=int(input("Enter Divisor"))
    ans=a/b
    print("Answer = ",ans)

else:
    print("Invalid input")