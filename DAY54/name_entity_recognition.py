import re 
import nltk
from nltk.tokenize import word_tokenize

#sample text
text = "John Doe is the CEO of OpenAI . He lives in San Francisco."

#Lexicons for different entity types
person_lexicon = {"John Doe","Alice","Bob"}
organization_lexicon = {"OpenAI","Google","Microsoft"}
location_lexicon = {"San Francisco","New York","Los Angeles"}

def lexicon_based_ner(text):
    entities =[]
    tokens = word_tokenize(text)
    for token in tokens:
        if token in person_lexicon:
            entities.append((token, "PERSON"))
        elif token in organization_lexicon:
            entities.append((token,"ORG"))
        elif token in location_lexicon:
            entities.append((token,"LOC"))
    return entities
print("Lexicon-based NER: ")
print(lexicon_based_ner(text))
