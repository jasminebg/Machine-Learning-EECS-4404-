import numpy as np

#all unique words and list of docs in corpus
def Unique(filename):
    #enwiki8 doc
    #Getting count of all words
    uniquecount = {}
    documents = []
    with open(filename,'r',encoding='utf-8') as file:
        for line in file:
          #wordfreq = {}
          for word in line.strip().split():
            if word in uniquecount:
              uniquecount[word] +=1
            else:
              uniquecount[word] = 1
          #document = list(wordfreq.values())
          documents.append(line.strip().lower())
    return uniquecount, documents
#Top10k~ words + humanscores
def Top10k(terms):
    #Getting top 10k words
    top10k = dict(sorted(terms.items(), key=lambda x:x[1], reverse=True)[:10000])
    #print(len(top10k))
    #print(top10k)
    humanscores = []
    with open("wordsim353_human_scores.txt",'r',encoding='utf-8') as file:
        for line in file:
            humanscores.append(line.strip().split())
            word1, word2, sc = line.strip().split()
            if(word1 in uniquecount and word1 not in top10k):
                    top10k[word1] = uniquecount[word1]
            if(word2 in uniquecount and word2 not in top10k):
                    top10k[word2] = uniquecount[word2]           
                
    #assigning row to each word in the top 10k words
    return top10k, {k:v for v,k in enumerate(list(top10k.keys()))}, humanscores
    #print(wordrows)
#DocWordFreq matrix
def dwf(docs, top10k, wordrows):
    docwordfreq = np.zeros((len(top10k),len(docs)))
    for docnum in range(len(docs)):
        doc = {}
        for word in docs[docnum].strip().split():
            if word in top10k:
                if word in doc:
                    doc[word]+=1
                else:
                    doc[word] = 1
        for word in doc.keys():
            docwordfreq[wordrows[word]][docnum] = doc[word]
    docwordfreq = np.asarray(docwordfreq)
    return docwordfreq


print("Part 1 started... ")
uniquecount,docs = Unique("enwiki8.txt")
print("Unique count of all terms obtained")
top10k, wordrows, humansc = Top10k(uniquecount)
print("Top 10,000 terms and row# for all words obtained")
docwords = dwf(docs, top10k, wordrows)
print("Documemt Word Frequency Matrix obtained, shape of matrix: ")
print(docwords.shape)
#Uses ~8gb RAM
print("Part 1 completed")