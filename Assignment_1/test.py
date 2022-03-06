ip= input('Enter the file name: ')
punc="""@_,.$#%&^!~*?:;"{[}]/\|`<>()+="""
punc1="""'-"""
print ('Reading', ip, '...')
with open(ip) as f:
    txt=f.read().strip()
# Cleaning text and lower casing all words
for char in punc:
    txt=txt.replace(char,' ')
print(txt)    
txt = txt.lower()
# split returns a list of words delimited by sequences of whitespace (including tabs, newlines) 
word_list = txt.split()
print(word_list)

# Initializing Dictionary
d = {}

# Count number of times each word comes up in list of words (in dictionary)
for word in word_list:
    if len(word)==1 and word in punc1:
        continue
    else:
        if word[-1:] in punc1:
            word=word[:-1]
            print("if1")
            print(word)
        if word[0] in punc1:
            print("if2")
            word=word[1:]
            print(word)
        if word not in d:
            print("if3")
            d[word] = 0
            print(word)
        d[word] += 1
        
print(d)

#reverse the key and values so they can be sorted using tuples.
word_freq = []
for key, value in d.items():
    word_freq.append((value, key))
print(word_freq)
word_freq.sort(reverse=True)
print(word_freq)
f.close()
file=input("Name the Output File: ")
fout=open("{}.csv".format(file),'w')
for word in word_freq:
    fout.write("{},{}\n".format(word[1],word[0]))

fout.close()
