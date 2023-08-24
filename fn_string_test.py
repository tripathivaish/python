def string_test(s):
    d={"upper_case":0,"lower_case":0}
    for i in s:
        if i.isupper():
            d["upper_case"]+=1
        elif i.islower():
            d["lower_case"]+=1
        else:
           pass
    print("the string is",s)
    print("total uppercase characters are=",d["upper_case"])
    print("total lowercase characters are=",d["lower_case"])
string_test("the black BROWN FOX is running Behind THE JUNGLE")