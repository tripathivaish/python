a=[]
n=int(input("enter the length of the list"))
for i in range(0,n):
    ele=(input("enter the element\n"))
    a.append(ele)
    print(".....................................................")
a.sort(key=len)                            #most important part
print(a)