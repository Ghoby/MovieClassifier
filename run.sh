#!/bin/bash
#Group 11

#Preprocessing
tr '[:upper:]' '[:lower:]' < $1 > PPCorpus1.txt			#lowercasing
tr '[:upper:]' '[:lower:]' < $2 > PPTeste1.txt			
tr -d '[\?\!\.\:\,\-]' < PPCorpus1.txt > PPCorpus2.txt	#remove ? ! .
tr -d '[\?\!\.\:\,\-]' < PPTeste1.txt > PPTeste2.txt	
tr -d "\'" < PPCorpus2.txt > PPCorpus3.txt				#remove '
tr -d "\'" < PPTeste2.txt > PPTeste3.txt		
tr '\t' ' ' < PPCorpus3.txt > PPCorpus4.txt				#tab-> space
tr '\t' ' ' < PPTeste3.txt > PPTeste4.txt		
tr -s ' ' < PPCorpus4.txt > PPCorpus5.txt				#remove extra spaces
tr -s ' ' < PPTeste4.txt > PPTeste5.txt
python3 lemm.py PPCorpus5.txt							#lemmatization (Stemming alternative)
python3 lemm.py PPTeste5.txt
sort PPCorpus5.txt > PPCorpus6.txt						#sort By tag name (alphabetical)


#create file with every word in the corpus separated by line (no duplicates)
cut -d ' ' -f2- PPCorpus6.txt > WordListing1.txt									#remove tags	
tr -sc 'A-Za-z|A-Za-z\-A-Za-z' '\n' < WordListing1.txt > WordListing2.txt			#separate words
sort WordListing2.txt | uniq > WordListing3.txt										#prder alphabetically and remove duplicates

#classification process
python3 classifier.py WordListing3.txt PPCorpus6.txt PPTeste5.txt					#ti-idf inspired solution (main solution)
#python3 jaccardbaseline.py PPCorpus6.txt PPTeste5.txt								#Jaccard 
#python3 dicebaseline.py PPCorpus6.txt PPTeste5.txt									#Dice
