'''fname=input("enter the file name")
ele=input("enter the word to be searched")
count=0
with open(fname,'r') as f1:
    for line in f1:
        words=line.split(" ")
        for i in words:
            if(i==ele):
                count=count+1
print("the number of occurance",count)'''
'''count=0
with open("a.txt","r") as f1:
    for line in f1:
        count=count+1
    print("the total number of lines are=",count)'''

'''str=input("enter the string to be added in file")

f1= open("C:\\Users\\VAISHNAVI TRIPATHI\\Desktop\\python programming (1)\\a.txt","a+")
f1.write(str)
f2= open("C:\\Users\\VAISHNAVI TRIPATHI\\Desktop\\python programming (1)\\a.txt","r")
print(f2.read())
        '''
'''with open("a.txt","r") as f1:
    with open("b.txt","w") as f2:
        for line in f1:
            f2.write(line)'''
'''count=0
fname=input("enter the file name")
ele=input("enter the letter")
with open(fname,"r") as f1:
    for line in f1:
        word=line.split(" ")
        for i in word:
            for letter in i:
                if(letter==i):
                    count=count+1
print("occurence of letter",count)
    data=f1.read()
    for i in data:
        if(ele==i):
            count=count+1
    print(count)
'''
'''fname=input("enter the file name=")
ccount=0 
w_count=0
l_count=0
f1=open(fname,"r")
c_data=f1.read()
for i in c_data:
    ccount=ccount+1
print("number of characters",ccount)
w_data=c_data.split(" ")
for i in w_data:
    w_count=w_count+1
print("no of words=",w_count)
c_data=f1.seek(0)
l_data=f1.readlines()
for i in l_data:
    l_count=l_count+1
print("no of lines",l_count)
'''

'''matrix=[]
matrix.append(3*[1])
matrix.append(3*[1])
matrix.append(3*[1])
matrix[0][0]=2
print(matrix)'''

'''score=[30,1,2,1,0]
print(score.index(1))'''





'''count=0
l=[1,2,3,4,5]
if (l==sorted(l)):
    count=1
if(count):
    print("yes,list is sorted")
else:
    print("no")
'''
'''t=(2,'heloo',[2,33],{1,5})
t[-1].add(1.0)
t[-2][0]='hi'
print(t)
'''

'''details={1:'john',16:'jill',109:"joe",145:"jack"}
num=len(details)
print(num)
print(details)
details.pop(145)
print(details)
sort_data=sorted(details.items(),key=lambda x:x[1])
dict=dict(sort_data)
print(dict)'''

'''tup=(2,[2,2],2)
tup[1][1]=5
print(tup)'''

'''import string
alphabet=set(string.ascii_lowercase);
alphabet2=set(string.ascii_uppercase)
str="abcdefghijklmnopqrstuvwxyZABCDEFGHIJKLMNOPQRSTUVWXYz"
if(set(str.lower())>=alphabet) or (set(str.upper())>=alphabet2):
    print("exists")
else:
    print("not exist")'''


with open("a.txt",'r') as f1:
    
    for line in range(0,3):
        data=f1.readline()
        print(data)

