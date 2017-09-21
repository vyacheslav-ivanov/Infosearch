def inverted_ind(doc):
    d = {}
    for n in range(0, len(doc)):
        for term in doc[n]:
            if term not in d:
                d[term] = [n+1]
            else:
                d[term].append(n+1)
    return d
    

doc_1 = ['I', 'was', 'at', 'home']
doc_2 = ['what', 'was', 'I', 'doing']
doc_3 = ['I', 'was', 'doing', 'my', 'homework']

print(inverted_ind([doc_1, doc_2, doc_3]))
