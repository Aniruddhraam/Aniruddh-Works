#Cylinder
import math
print("PLEAST MAKE SURE ALL UNITS ARE THE SAME")
input("PRESS ENTER TO START")
print("CSA-->1")
print("TSA-->2")
print("VOLUME-->3")

choice=int(input("ENTER A VALUE FROM 1-3="))

if choice==1:
    r=float(input("ENTER RADIUS"))
    h=float(input("ENTER HEIGHT"))
    CSA=2*math.pi*r*h
    print("CSA=",CSA)


if choice==2:
    r=float(input("ENTER RADIUS"))
    h=float(input("ENTER HEIGHT"))
    TSA=2*math.pi*r*(h+r)
    print("TSA=",TSA)

if choice==3:
    r=float(input("ENTER RADIUS"))
    h=float(input("ENTER HEIGHT"))
    VOLUME=math.pi*r*r*h
    print("VOLUME=",VOLUME)

input()
