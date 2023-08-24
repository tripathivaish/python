num1=int(input("enter the first number"))
num2=int(input("enter the second number"))
if(num1>num2):
    small=num2
elif(num1<num2):
    small=num1
for i in range(1,small+1):
    if(num1%i==0 and num2%i==0):
        count=i

print("the gcd is=",count)