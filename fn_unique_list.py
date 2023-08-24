def list(l):
    uni_list=[]
    for i in l:
        if i not in uni_list:
            uni_list.append(i)
    print(uni_list)
list([3,3,5,6,1,2,7,7,7,7,9])