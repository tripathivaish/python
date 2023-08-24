L=[500,200,100,50,20,10,2,1]
total=int(input("the amount is"))
for i in range (8):
    count=total//L[i]
    print(L[i],":",count)
    rem=total%L[i]
    total=rem

