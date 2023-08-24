def factorial(num):
    if num==0:
        return 1
    else:
        return num*factorial(num-1)  
num=int(input("enter the number to be calculated"))
print(factorial(num))