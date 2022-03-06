file = open("Dataset-1.csv", 'r',encoding="utf8")
of=input("Name the Output File: ")
while 1:
    lines=file.readlines(10000)
    for line in lines:
        data = line.rstrip()
        data = data.split(",")
        #print(data[1:])
        #print("\nThe student you require is: {} {} \n".format(data[0],data[1:]))
        punc="""@_,.$#%&^!~*?:;"{[}]/\|`<>()+="""
        punc1="""'-"""
        # Cleaning text and lower casing all words
        txt=" ".join(str(x) for x in data[1:])
        
        for char in punc:
            txt=txt.replace(char,' ')
            #print(txt)
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
                    if word[0] in punc1:
                        word=word[1:]
                    if word not in d:
                        d[word] = 1
                    d[word] += 1
            print(d)

            #reverse the key and values so they can be sorted using tuples.
            word_freq = []
            for key, value in d.items():
                word_freq.append((value, key))
            print(word_freq)
            word_freq.sort(reverse=True)
            print(word_freq)
            file.close()   
        
            fout=open("{}.csv".format(of),'w')
        for word in word_freq:
            fout.write("{},{},{}\n".format(data[0],word[1],word[0]))

fout.close()

#file.close()
