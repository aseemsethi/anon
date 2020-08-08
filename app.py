#https://spacy.io/api/annotation#named-entities
import spacy
from pprint import pprint
import tabulate

from anonymize import Anonymize

spacy_tags_to_anon = ['PERSON', 'ORG', 'GPE', 'NORP', 'FAC', 'DATE', 'TIME']
custom_tags_to_anon = ['COURSE', 'CONTACT', 'EMAIL']
anon = Anonymize(spacy_tags_to_anon, custom_tags_to_anon)

origS = ["Aseem Sethi took ISO27001 got a score of 70.1. He joined in Jan 2020 \
Birla Institute of Technology located at Pilani, Rajasthan, India. His \
ema is a@b.com."]
anonS = [anon.get_anon_string(origs) for origs in origS]
for idx in range(len(origS)):
    to_print = tabulate.tabulate(zip(anon.tokenize(origS[idx]), anonS[idx].split()), \
                             headers = ["Original String", "Anonymized String"])
print(to_print)
print("*"*50)
pprint(anon.mapping)
print("*"*50)
print("Anon String: ", anonS)