'''printing first and lasT ELSEMENT OF THE PROGRAM'''
list=[]

n=int(input("enter the number of an elements stored in list"))
for i in range(n):
    elements=int(input("enter the element-"))
    list.append(elements)
print(list)
print("the first element is- ",list[0],"the last element is- ",list[-1])