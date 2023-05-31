import nltk

sentence = "Ade is moving"

tokens = nltk.word_tokenize(sentence)

tagged = nltk.pos_tag(tokens)

patterns= """mychunk:{<NN.?>*<VBD.?>*<JJ.?>*<CC>?}"""

chunks = nltk.RegexpParser(patterns)

output = chunks.parse(tagged)

print("Tagged: ",tagged)

print()
print("Chunks: ",output)