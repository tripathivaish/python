import random
a=[]
n=int(input("enter the length of list"))
for i in range(n):
    ele=random.randint(1,100)
    a.append(ele)
print(a)