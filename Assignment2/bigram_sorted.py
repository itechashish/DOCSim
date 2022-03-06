ip= input('Enter the file name: ')
punc="""@_,.$#%&^!~*?:;"{[}]/\|`<>()+="""
punc1="""'-"""
print ('Reading', ip, '...')
with open(ip) as f:
    txt=f.read().strip()
# Cleaning text and lower casing all words
for char in punc:
    txt=txt.replace(char,' ')
txt = txt.lower()
#print(txt)
# split returns a list of words delimited by sequences of whitespace (including tabs, newlines) 
word_list = txt.split()
print(word_list)
l=len(word_list)
biword_freq = {}
#print(l)
for word in word_list:
    if len(word)==1 and word in punc1:
        continue
    else:
        if word[-1:] in punc1:
            word=word[:-1]
        if word[0] in punc1:
            word=word[1:]
    #print(word)   
for i in range(l-1):
    biword = (word_list[i], word_list[i+1])
    if biword not in biword_freq:
        biword_freq[biword] = 0
    biword_freq[biword] += 1  
print(biword_freq)
bi_word=[]
for key, value in biword_freq.items():
    bi_word.append((value, key))
#print(bi_word)
bi_word.sort(reverse=True)
print(bi_word)
f.close()
file=input("Name the output File:")
fout=open("{}.csv".format(file),'w')
for bigram in bi_word:
    fout.write("{} , {}\n".format(bigram[0],bigram[1]))
fout.close()
