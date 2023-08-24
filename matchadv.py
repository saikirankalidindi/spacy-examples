import spacy 
from spacy.matcher import Matcher

nlp = spacy.load('en_core_web_sm')

matcher = Matcher(nlp.vocab)

doc = nlp('i want butter cone')

pattern = [{'lemma':'want','pos':'VERB'},{'pos':'NOUN','op':'*'}]

matcher.add('vest',[pattern])

matches = matcher(doc)

for id,start,end in matches:
    print(doc[start:end])

