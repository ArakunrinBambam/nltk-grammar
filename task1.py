import nltk

grammar = nltk.CFG.fromstring("""
    S -> NP VP
    NP -> NN | DT NN
    VP -> V | V NP 
""")

sentence = input("Supply the sentence to check: ")

tokens = nltk.word_tokenize(sentence)

tagged = nltk.pos_tag((tokens))

print(tagged)


nouns = [word for (word, pos) in tagged if pos.startswith('N') or pos.startswith('PRP')]
verbs = [word for (word, pos) in tagged if pos.startswith('V') or pos.startswith('TO')]
deters = [word for (word, pos) in tagged if pos.startswith('DT') or pos.startswith('IN')]


production_rules = []

for n in nouns:
    production_rules.append(nltk.Production(nltk.Nonterminal('NN'), [n]))
for v in verbs:
    production_rules.append(nltk.Production(nltk.Nonterminal('V'), [v]))
for d in deters:
    production_rules.append(nltk.Production(nltk.Nonterminal('DT'), [d]))


updated_grammar = nltk.CFG(grammar.start(), grammar.productions() + production_rules)

# print(updated_grammar)

parser = nltk.ChartParser(updated_grammar)


is_accepted = False

for tree in parser.parse(tokens):
    is_accepted = True
    break


if is_accepted :
    print("The Supply Sentence is grammatically correct")
else:
    print("The Supplied Sentence is NOT grammatically correct")



