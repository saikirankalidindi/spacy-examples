import spacy 
from spacy.matcher import Matcher

nlp = spacy.load('en_core_web_sm')

text = 'sai is a good developer'

matcher = Matcher(nlp.vocab)

doc = nlp(text)

pattern = [{'TEXT':'sai'}]

matcher.add('name',[pattern])

matches = matcher(doc)

for match_id, start,end in matches:
    print(doc[start:end])