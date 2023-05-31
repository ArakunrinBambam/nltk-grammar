import nltk

grammar = nltk.CFG.fromstring("""
   S -> Number
   Number -> Digit | Number Digit
   Digit -> 0
   Digit -> 1 
   Digit -> 2
   Digit -> 3
""")

parser = nltk.ChartParser(grammar)

string = input("Supply the string to check: ")

words = nltk.word_tokenize(string)
trees = list(parser.parse(words))
