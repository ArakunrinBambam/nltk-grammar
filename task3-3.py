import nltk

grammar = nltk.CFG.fromstring("""
    SENTENCE -> NP VP
    NP -> Det N | Det N PP
    VP -> V NP | V NP PP
    PP -> P NP
    NP -> 'I'
    N -> 'man' | 'park' | 'telescope' | 'dog'
    Det -> 'the' | 'a'
    P -> 'in' | 'with'
    V -> 'saw'
""")