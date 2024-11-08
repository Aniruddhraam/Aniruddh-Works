import math
print("MAKE SURE THAT ALL THE UNITS ARE THE SAME")
print("PRESS ENTER TO CONTINUE")
input()
print("CSA-->1")
print("TSA-->2")
print("VOLUME-->3")

choice=int(input("ENTER A VALUE FROM 1-3="))

if choice==1:
    l=float(input("ENTER THE VALUE OF L"))
    r=float(input("ENTER RADIUS"))
    h=float(input("ENTER HEIGHT"))
    csa=math.pi*r*l
    print("CSA=",csa)

if choice==2:
    l=float(input("ENTER THE VALUE OF L"))
    r=float(input("ENTER RADIUS"))
    h=float(input("ENTER HEIGHT"))
    tsa=math.pi*r*(l+r)
    print("TSA=",tsa)

if choice==3:
    r=float(input("ENTER RADIUS"))
    h=float(input("ENTER HEIGHT"))
    volume=1/3*math.pi*r*r*h
    print("VOLUME=",volume)

input()
