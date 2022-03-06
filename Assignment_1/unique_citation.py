ip= input('Enter the file name: ')
punc="""@_,$#%&^!~*?/.:;'-"{[}]\|`<>()+=""" 
print ('Reading', ip, '...')
with open(ip,'r') as f:
    txt=f.read().strip().split()
wordcount={}
for word in txt:
    if word[-1:] in punc:
        word=word[:-1]
    if word[0] in punc:
        word=word[1:]
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1
        
keys = list(wordcount.keys())
keys.sort()

file=input("Name the Output File: ")
fout=open("{}.csv".format(file),'w')
for word in keys:
    fout.write("{},{}\n".format(word,wordcount[word]))
fout.write("\r\n")
fout.close()
