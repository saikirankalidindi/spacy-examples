import spacy 
from spacy.language import Language

@Language.component('length')
def com_len(doc):
    length = len(doc)

    return doc

nlp = spacy.load('en_core_web_sm')

nlp.add_pipe('length',first=True)

print(nlp.pipe_names)

# print(nlp.pipeline)

