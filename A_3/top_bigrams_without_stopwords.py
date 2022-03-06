import nltk
from nltk.corpus import stopwords
ip= open("Dataset-1.csv", 'r',encoding="utf8")
k=int(input("Input K value: "))
file=input("Name the Output File: ")
punc="""@_,.$#%&^!~*?:;"{[}]/\|`<>()+="""
punc1="""'-"""
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
#print(stopwordsfree_words)
l=len(stopwordsfree_words)
# Initializing Dictionary
biword_d= {}
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
            
#print(biword_d)
for i in range(l-1):
    biword = (stopwordsfree_words[i], stopwordsfree_words[i+1])
    if biword not in biword_d:
        biword_d[biword] = 0
    biword_d[biword] += 1  
print(biword_d)
bi_word=[]
for key, value in biword_d.items():
    bi_word.append((value, key))
#print(bi_word))
bi_word.sort(reverse=True)
#print(bi_word)
ip.close()
fout=open("{}.csv".format(file),'w',encoding="utf8")
#fout.write("{} \n".format(maxkeys))
for biword in bi_word:
    fout.write("{},{}\n".format(biword[1],biword[0]))
    k=k-1
    if k==0:
        break
fout.close()

