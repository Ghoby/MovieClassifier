import fileinput 
import sys
import re

def diceDistance(corpus, test):
	with open(corpus, 'r') as corpusFile:		
		with open(test, 'r') as testFile:
			
			for testLine in testFile:
				wordsInTestLine = set(testLine.replace('\n', '').split(' '))
				outTag = ""
				highestValue = 0
				for corpusLine in corpusFile:
					wordsInCorpusLine = re.sub("[^\w]", " ", corpusLine.replace('\n', '')).split()
					

					#print(list(wordsInCorpusLine[0]))
					tag = wordsInCorpusLine.pop(0)
					intersection = set(wordsInTestLine).intersection(wordsInCorpusLine)
					diceValue = 2 * len(intersection) / (len(wordsInCorpusLine) + len(wordsInTestLine))
					if (highestValue < diceValue or outTag == ""):
						highestValue = diceValue
						outTag = tag
				
				corpusFile.seek(0)
				print(outTag)
	return



diceDistance(sys.argv[1],sys.argv[2])
