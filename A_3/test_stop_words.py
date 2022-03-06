a=['ashish','a','kumar','b','x','9','bc','kr','k']
'''for word in a:
    if len(str(word))==1:
        a.remove(word)
print(a)'''
a=[i for i in a if len(i)>1]
'''iterated=0
removed=0
for word in a:
    iterated+=1
    if len(word)==1:
        a.remove(word)
        removed+=1'''
print(a)
#print(iterated)
#print(removed)

