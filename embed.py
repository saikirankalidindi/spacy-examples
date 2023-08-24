import spacy
from gensim.models import Word2Vec

# define training data
data = '''Computers and machines are great at working with tabular data or spreadsheets. However, as human beings generally communicate in words and sentences, not in the form of tables. Much information that humans speak or write is unstructured. So it is not very clear for computers to interpret such. In natural language processing the goal is to make computers understand the unstructured text and retrieve meaningful pieces of information from it. Natural language Processing is a subfield of artificial intelligence, in which its depth involves the interactions between computers and humans.'''


nlp = spacy.load('en_core_web_lg')

doc = nlp(data)

# vector = doc.vector

# print(vector)

for token in doc:
    print(token.text, token.has_vector,token.vector_norm)
