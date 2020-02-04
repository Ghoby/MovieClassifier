import fileinput 
import sys
import numpy as np
import math

TAG = 16
TAG_ARRAY = np.array(["actor_name","budget","character_name","genre","keyword","original_language","original_title","overview",
					"person_name","production_company","production_country","release_date","revenue","runtime","spoken_language",
					"vote_avg"])

#####AUX FUNCTIONS######
def createArray(words):
	i=0
	for line in fileinput.input(words):
		line = line.replace('\n', '')
		i+=1
	array = np.zeros((i,TAG))
	return array

def countWordInSentence(word, sentence):
	sentenceWords = sentence.replace('\n', '').split(' ')
	occurences = 0 
	for i in sentenceWords:
		if i == word:
			occurences+=1
	return occurences

def idfaux(array):
	sumOccurences = np.zeros((array.shape[0]))

	for i in range(array.shape[0]):
		numberOfOccurences = 0
		for j in range(array.shape[1]):
			if array[i,j] > 0:
				numberOfOccurences += 1
		sumOccurences[i] = numberOfOccurences
	return sumOccurences
#########################


def rawCount(words, corpus, array):

	with open(corpus, 'r') as corpusFile:
		wordCount = 0
		for word in fileinput.input(words):
			word = word.replace('\n', '')
			columnCount = 0
			tag = ""
			
			for corpusLine in corpusFile:
				currentTag = corpusLine.split(' ', 1)[0]
				
				if tag == "":
					tag = currentTag
	
				elif tag != currentTag:
					tag = currentTag
					columnCount += 1

				wordOccurences = countWordInSentence(word, corpusLine)
				if wordOccurences > 0:
					array[wordCount, columnCount] += wordOccurences

			wordCount += 1
			corpusFile.seek(0)

	return array


def tfidf(array):
	
	sumColumn = np.sum(array, axis=0)
	sumOccurencesRow = idfaux(array)
	frequencyArray = np.zeros((array.shape[0], array.shape[1]))
	numberOfTags = array.shape[1]
	cont = 0
	for a in sumOccurencesRow:
		if a==0:
			print (cont)
		cont+=1
	for i in range(array.shape[0]):

		for j in range(array.shape[1]):
			tf = array[i,j]	/ sumColumn[j]
			idf = math.log10(numberOfTags / sumOccurencesRow[i])

			frequencyArray[i,j] = tf * idf
	return frequencyArray



def evaluation(test, wordsFile, freqArray):
	with open(test, 'r') as testFile:		
		with open(wordsFile, 'r') as wordList:
			
			i = 0
			for j in testFile:
				i+=1
			outputArray = np.full((i), '')
			sentence_counter = 0
			testFile.seek(0)

			for sentence in testFile:
				tagValueArray = np.zeros((16))

				wordsInSentence = set(sentence.split(' '))
		
				for wordInSentence in wordsInSentence:
					i = 0
					for word in wordList:
						if wordInSentence.replace('\n', '') == word.replace('\n', ''):
							tagIndex = np.argmax(freqArray[i])
							tagValue = np.amax(freqArray[i])
							tagValueArray[tagIndex] += tagValue
							if wordInSentence.replace('\n', '') in TAG_ARRAY[tagIndex]:
								tagValueArray[tagIndex] += 0.1
							break
						i+=1
					wordList.seek(0)

				tag = TAG_ARRAY[np.argmax(tagValueArray)]
				print(tag)
				outputArray[sentence_counter] = tag
				sentence_counter += 1





emptyCountArray = createArray(sys.argv[1])
rawCountArray = rawCount(sys.argv[1], sys.argv[2],emptyCountArray)

freqArray = tfidf(rawCountArray)

evaluation(sys.argv[3], sys.argv[1], freqArray)





