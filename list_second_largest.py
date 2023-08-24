a=[]
n=int(input("enter  the length of list"))
for i in range(n):
    ele=int(input("enter the element\n"))
    a.append(ele)
    a.sort()
print("second largest number",a[-2])

