import spacy 

nlp = spacy.load('en_core_web_sm')

data = open('data.txt').read()

doc =  nlp(data)
           
doc = [token for token in doc if not token.is_punct and not token.is_stop]

doc = [token for token in doc if not token.pos_ == 'X']


