cp = float(input("Enter cost price:"))
sp = float(input("Enter selling price:"))

if(sp > cp):
    print("profit.")
elif(cp > sp):
    print("loss.")
else:
    print("No profit,No loss")