str=input("the string is-")
l=[]
l=str.split()
for p in l:
    wordfreq=[l.count(p)]
print(dict(zip(l,wordfreq)))