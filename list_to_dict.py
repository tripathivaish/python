key=[]
values=[]
n=int(input("enter the number of elements"))
for i  in range(0,n):
    ele=input("enter the keys")
    key.append(ele)
for j in range(0,n):
    ele=int(input("enter the values"))
    values.append(ele)
d={}
d=dict(zip(key,values))
print(d)