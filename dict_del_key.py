d={}
data=int(input("enter the total no of students"))
for i in range(data):
    name=input("enter the name of student")
    marks=int(input("enter the marks"))
    d[name]=marks
    i=i+1

ele=input("enter the students to be deleted")
print("data before deletion",d)
if ele in d:
    del d[ele]
print("the updated data is-",d)