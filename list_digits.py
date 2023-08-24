ub=int(input("enter the upperbound"))
lb=int(input("enter the lowebound"))
for i in range(lb,ub+1):
   
    digit=i%10
    sum+=i
    if sum<10:
        print("these are the elements whose sum of digits are less than 10  ",i)
