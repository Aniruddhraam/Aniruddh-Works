#CONE
from math import sqrt
import math
print("CALCULATING THE VALUE OF L")
r=float(input("ENTER RADIUS"))
h=float(input("ENTER HEIGHT"))
x=h**2+r**2
l=sqrt(x)
print("L=",l)
print("VALUE OF L IS SAVED")
print("CSA-->1")
print("TSA-->2")
print("VOLUME-->3")

choice=int(input("ENTER A VALUE FROM 1-3="))

if choice==1:
    r=float(input("ENTER RADIUS"))
    h=float(input("ENTER HEIGHT"))
    csa=math.pi*r*l
    print("CSA=",csa)

if choice==2:
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
