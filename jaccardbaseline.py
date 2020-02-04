import fileinput 
import sys
import re

def jaccardDistance(corpus, test):
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
					union = set(wordsInTestLine).union(wordsInCorpusLine)
					intersection = set(wordsInTestLine).intersection(wordsInCorpusLine)
					jaccardValue = len(intersection) / len(union)
					if (highestValue < jaccardValue or outTag == ""):
						highestValue = jaccardValue
						outTag = tag
				
				corpusFile.seek(0)
				print(outTag)
	return



jaccardDistance(sys.argv[1],sys.argv[2])
