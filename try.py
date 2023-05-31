import nltk
# grammar = nltk.CFG.fromstring("""
#     S -> NP VP
#     PP -> P NP
#     NP -> Det N | NP PP
#     VP -> V NP | VP PP
#     Det -> 'a' | 'the'
#     N -> 'dog' | 'cat'
#     V -> 'chased' | 'sat'
#     P -> 'on' | 'in'
# """)
grammar = nltk.CFG.fromstring("""
    S -> NP VP
    NP -> NN | DT NN
    VP -> V | V NP 
    NN -> 'cat' | 'dog'
    V -> 'chased' | 'ate'
""")

tokens = nltk.word_tokenize("I saw a man in the park")

tagged = nltk.pos_tag(tokens)

# brown_corpus = nltk.corpus.brown

# Filter and extract only the nouns from the corpus
# nouns = [word for (word, pos) in brown_corpus.tagged_words() if pos.startswith('N')]
nouns = [word for (word, pos) in tagged if pos.startswith('NN')]

# Print the extracted nouns
print(nouns)  # Print the first 20 nouns

#grammar = nltk.CFG.fromstring(grammar)

# Load a corpus (e.g., sentences) to be incorporated into the grammar
# corpus = nltk.corpus.brown.sents()[:100]
# production_rules = []

# for sentences in corpus:
#     my_string = ' '.join(str(x) for x in sentences)
#     tt = nltk.word_tokenize(my_string)
#     tg = nltk.pos_tag(tt)
#     print(tg[1])

        # tag = nltk.pos_tag(sentence)
        # print(tag)

# updated_grammar = nltk.CFG(grammar.start(), grammar.productions() + production_rules)
# print(updated_grammar)
# parser = nltk.parse.RecursiveDescentParser(grammar)
# parser = nltk.parse.ShiftReduceParser(grammar, trace=2)
#parser = nltk.ChartParser(grammar)

# result = parser.parse(tokens)

# result.draw()
# for p in parser.parse(tagged):
#     print(p)

# grammar.start()


# grammar.productions()


