import spacy
import pathlib

filename = 'data.txt'

nlp = spacy.load('en_core_web_sm')

intro_doc = nlp(pathlib.Path(filename).read_text(encoding='utf-8'))

doc = nlp('this is a sample text for spacy production management.')

print([token.text for token in doc])

sentences = list(doc.sents)

print([sentence.text for sentence in sentences])

