import nltk
#nltk.download('wordnet') #INFORMAR A STORA QUE TEM DE INSTALAR A PACKAGE

from nltk.stem.wordnet import WordNetLemmatizer 
import fileinput 
import sys

# Method inspired by -> https://stackoverflow.com/questions/49341740/lemmatizing-txt-file-and-replacing-only-lemmatized-words 
#						https://pythonprogramming.net/lemmatizing-nltk-tutorial/						

lmtzr = WordNetLemmatizer()

def lemmFunction(outputText):
	for line in fileinput.input(outputText, inplace=True):
		line = ' '.join([lmtzr.lemmatize(w) for w in line.rstrip().split()])
		print(line)
	return 


lemmFunction(sys.argv[1])
