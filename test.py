import nltk

nltk.download()


sentence = """At eight o'clock on Thursday morning Authur didn't feel very good"""

tokens = nltk.word_tokenize(sentence)

print(tokens)

tagged = nltk.pos_tag(tokens)

tagged[0:6]

entities = nltk.chunk.ne_chunk(tagged)

entities