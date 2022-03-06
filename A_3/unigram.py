ip= open("sample_Dataset-1.csv", 'r',encoding="utf8")
k=int(input("Input K value: "))
file=input("Name the Output File: ")
punc="""@_,.$#%&^!~*?:;"{[}]/\|`<>()+="""
punc1="""'-"""
#print ('Reading', ip, '...')
#with open(ip) as f:
#txt=ip.read().strip()
lines=ip.readlines()
word_list=[]
for line in lines:
    data=line.rstrip()
    txt=data
    #print(txt)'''
#print(txt)
   
 # Cleaning text and lower casing all words
    for char in punc:
        txt=txt.replace(char,' ')
        #print(txt)
    txt = txt.lower()
    #print(txt)
    # split returns a list of words delimited by sequences of whitespace (including tabs, newlines)
    a=txt.split()
    
    word_list.extend(a)
    
#print(word_list)

# Initializing Dictionary
d = {}

# Count number of times each word comes up in list of words (in dictionary)
for word in word_list:
    if len(word)==1 and word in punc1:
        continue
    else:
        if word[-1:] in punc1:
            word=word[:-1]
        if word[0] in punc1:
            word=word[1:]
        if word not in d:
            d[word] = 0
        d[word] += 1
#print(d)
maxkeys = [k for k, v in d.items() if v == max(d.values())]
v=[max(d.values())]
maxkeys.append(v)
print(maxkeys)
#reverse the key and values so they can be sorted using tuples.
word_freq = []
for key, value in d.items():
    word_freq.append((value, key))
#print(word_freq))
word_freq.sort(reverse=True)
#print(word_freq)
#word_freq=str(str(word_freq).encode("utf8"))
#word_freq=word_freq.strip().split(",")
ip.close()
fout=open("{}.csv".format(file),'a+')
fout.write("{} \n".format(maxkeys))
for word in word_freq:
    fout.write("{},{}\n".format(word[1],word[0]))
    k=k-1
    if k==0:
        break
    
fout.close()

