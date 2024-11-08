ast= list(input("ENTER THE NUMBER LIST:-"))
newast=[]
for i in ast:
    if 1%2==0:
        newast+=[i]
if newast==[]:
    print("NO EVEN ELEMENT")
else:
    newast.sort()
    print("LARGEST EVEN NUMBER IN THE LIST IS:-", new1st[-1])
