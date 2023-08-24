import spacy 

# text = open('data.txt','r').read()
text = 'Donald Trump will meet the chairman of Google in New York City.'

nlp = spacy.load('en_core_web_lg')
# spacy pipeline
doc = nlp(text)

docs =[token.text for token in doc]

docList = [(token.text,token.pos_) for token in doc]

depList = [(token.text,token.dep_) for token in doc]
# 
entLabels = [(token.text,token.label_) for token in doc.ents]

# print(docs)
# print(docList)
# print(depList)
# Named Entity recognition-NER.
print(entLabels)