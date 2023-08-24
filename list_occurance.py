a=[]
n=int(input("enter the len of list"))

for i in range(n):
    word=input("enter the word")
    a.append(word)
print("the list is=",a)
count=0
c=[]
item=input("enter item to remove")
num=input("enter item occurance")
for i  in a:
    if(item==i):
        count=0
        count=count+1
        if count!=num:
            c.append(i)
        else:
            c.append(i)
    if(count==0):
        print("item not found")
    else:
        print("repation of word is:",count)
        print("updated list is",c)
        a=c

    