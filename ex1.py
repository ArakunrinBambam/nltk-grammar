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
# grammar = nltk.CFG.fromstring("""
#     S -> NP VP
#     NP -> Det N | Det N PP
#     VP -> V NP | V NP PP
#     PP -> P NP
#     NP -> 'I'
#     N -> 'man' | 'park' | 'telescope' | 'dog'
#     Det -> 'the' | 'a'
#     P -> 'in' | 'with'
#     V -> 'saw'
# """)




# tokens = nltk.word_tokenize("I saw a man in the park")

# # parser = nltk.parse.RecursiveDescentParser(grammar)
# # parser = nltk.parse.ShiftReduceParser(grammar, trace=2)
# parser = nltk.ChartParser(grammar)

# # result = parser.parse(tokens)

# # result.draw()
# for p in parser.parse(tokens):
#     print(p)

# # grammar.start()


# # grammar.productions()

import nltk

# Define the CFG grammar rules
grammar = nltk.CFG.fromstring("""
    S -> NP VP
    NP -> Det N
    VP -> V NP
    Det -> 'the' | 'a'
    N -> 'cat' | 'dog'
    V -> 'chased' | 'ate'
""")
                              
print(grammar)


# Create a parser based on the CFG grammar
parser = nltk.ChartParser(grammar)

def check_sentence(sentence):
    # Tokenize the sentence into a list of words
    words = nltk.word_tokenize(sentence)

    # Check if the sentence is accepted by the CFG grammar
    is_accepted = False
    for tree in parser.parse(words):
        is_accepted = True
        break

    return is_accepted

# Test the program
sentence1 = "the cat chased a dog"
sentence2 = "a dog ate the cat"

if check_sentence(sentence1):
    print("Sentence 1 is grammatically correct.")
else:
    print("Sentence 1 is grammatically incorrect.")

if check_sentence(sentence2):
    print("Sentence 2 is grammatically correct.")
else:
    print("Sentence 2 is grammatically incorrect.")
