import nltk
from nltk.corpus import stopwords
ip= open("Dataset-1.csv", 'r',encoding="utf8")
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
    #print(txt)
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
stop = stopwords.words('english')
stopwordsfree_words = [word for word in word_list if word not in stop and len(word)>1]   
print(stopwordsfree_words)

# Initializing Dictionary
d = {}

# Count number of times each word comes up in list of words (in dictionary)
for word in stopwordsfree_words:
    if len(word)==1 and word in punc1:
        continue
    else:
        for i in range(0,len(word)):
            if word[-1:] in punc1:
                word=word[:-1]
            elif word[0] in punc1:
                word=word[1:]
            else:
                break
        if word not in d:
            d[word] = 0
        d[word] += 1
word_freq = []
for key, value in d.items():
    word_freq.append((value, key))
#print(word_freq))
word_freq.sort(reverse=True)
print(word_freq)
ip.close()
fout=open("{}.csv".format(file),'w',encoding="utf8")
for word in word_freq:
    fout.write("{},{}\n".format(word[1],word[0]))
    k=k-1
    if k==0:
        break
fout.close()

