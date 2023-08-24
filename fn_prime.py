def prime(num):
    count=0
    for i in range(2,num-1):
        if num%i==0:
            count+=1
    if(count!=0):
        print("the number is not a prime number")
    else:
        print("this is a prime number")
num=int(input("enter the number to be found as the prime number"))
prime(num)