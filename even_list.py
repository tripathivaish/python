def even_list(l):
    even_list=[]
    for i in l:
        if i%2==0:
            even_list.append(i)
    print("the even numbers are,",even_list)
even_list([3,2,5,7,8,10,65,66,99,100])