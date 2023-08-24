def rev_string(str1):
    
        rstr=""
        index=len(str1)
        while(index>0):
            rstr+=str1[index-1]
            index=index-1
        print(rstr)
        return 0
print(rev_string("vaishnavi"))
