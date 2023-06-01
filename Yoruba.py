import nltk

grammar = nltk.CFG.fromstring("""
    S -> NP VP
    NP -> N | N DT 
    VP -> V | V NP 
    N -> 'baba' | 'iya' | 'egbon' | 'ana' | 'ile' | 'eniyan' | 'ebi' | 'Sola' | 'Julius' | 'oko' | 'kan' | 'mo' | 'moto' | 'awon'| 'obi' | 'Bola'
    V -> 'jade' | 'ni' | 'lo' | 'je' | 'ti' | 'to' 
    DT -> 'mi' |  'ti' | 're' | 'wa'

 
""")

string_in = input("Supply the Yoruba Sentence to check: ")

tokens = nltk.word_tokenize(string_in)

parser = nltk.ChartParser(grammar)


is_accepted = False

for tree in parser.parse(tokens):
    is_accepted = True
    break


if is_accepted :
    print("Sentence is accepted by grammar")
else:
    print("Sentence Not accepted")



