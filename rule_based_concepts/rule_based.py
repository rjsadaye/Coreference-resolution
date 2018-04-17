import os
import sys
import pickle
import subprocess
import nltk
import re
import time
import requests, json
from nltk.corpus import stopwords
from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize
from nltk.tokenize import PunktSentenceTokenizer
import requests,json

stopwords = stopwords.words('english')
st = StanfordNERTagger('/home/raj/Downloads/stanford-ner-2018-02-27/classifiers/english.all.3class.distsim.crf.ser.gz',
					   '/home/raj/Downloads/stanford-ner-2018-02-27/stanford-ner.jar',
					   encoding='utf-8')

person_list=['patient', 'the patient','doctor','the doctor','the boy','boy','the girl','girl','the man','man','the woman','woman','the lady','lady','person','the person','child','the child','infant','the infant']

sentence_re = r'(?:(?:[A-Z])(?:.[A-Z])+.?)|(?:\w+(?:-\w+)*)|(?:\$?\d+(?:.\d+)?%?)|(?:...|)(?:[][.,;"\'?():-_`])'
lemmatizer = nltk.WordNetLemmatizer()
stemmer = nltk.stem.porter.PorterStemmer()
grammar = r"""
	NBAR:
		{<NN.*|JJ>*<NN.*>}  # Nouns and Adjectives, terminated with Nouns
		
	NP:
		{<NBAR>}
		{<NBAR><IN><NBAR>}  # Above, connected with in/of/etc...
"""
chunker = nltk.RegexpParser(grammar)

def leaves(tree):
	"""Finds NP (nounphrase) leaf nodes of a chunk tree."""
	for subtree in tree.subtrees(filter = lambda t: t.label()=='NP'):
		yield subtree.leaves()

def normalise(word):
	"""Normalises words to lowercase and stems and lemmatizes it."""
	word = word.lower()
	# word = stemmer.stem_word(word) #if we consider stemmer then results comes with stemmed word, but in this case word will not match with comment
	word = lemmatizer.lemmatize(word)
	return word

def acceptable_word(word):
	"""Checks conditions for acceptable word: length, stopword. We can increase the length if we want to consider large phrase"""
	accepted = bool(2 <= len(word) <= 40
		and word.lower() not in stopwords)
	return accepted


def get_terms(tree):
	for leaf in leaves(tree):
		term = [ normalise(w) for w,t in leaf if acceptable_word(w) ]
		yield term

def get_noun_phrases(line):
	toks = nltk.regexp_tokenize(line, sentence_re)
	postoks = nltk.tag.pos_tag(toks)
	#print postoks
	tree = chunker.parse(postoks)
	terms = get_terms(tree)
	noun_list=[]
	for term in terms:
		for word in term:
			noun_list.append(word)
		
	return noun_list



path1 =sys.argv[1] #path to the docs folder

path2=sys.argv[2]   #path to the clamp output  folder

subprocess.call(['/home/raj/Downloads/ClampCmd_1.4.0/run_ner_pipeline.sh',path1,'clamp_out'])

all_files = os.listdir(path2)

all_files = [file for file in all_files if file.endswith('txt')]

sem_string = "semantic"

noun_pos=['NNP','NNPS','NN', 'NNS']

for i in os.listdir(path2):
	if i.endswith("txt"):	
		file = open("clamp_out/" + str(i))

		fp=open("concepts/"+i+".con","w+")

		clamp_concept=[]

		for line in file:
			if sem_string in line:

				line_list = line.split("\t")

				semantic = line_list[3].split("=")

				ne = line_list[5].split("=")

				fp.write(semantic[1]+','+ne[1])

				clamp_concept.append(ne[1])
		fp.write('\n')
		fp.close()

all_files=os.listdir(path1)
all_files = [file for file in all_files if file.endswith('txt')]

for i in os.listdir(path1):
	file=open(path1+"/"+i)
	fp=open("concepts/"+i+".con","a+")
	for line in file:
		noun_list=get_noun_phrases(line)
		for n in noun_list:
			if n in person_list:
				fp.write('person,'+n+'\n')

			#url = "https://api.genderize.io/?name="+n
			#response = requests.get(url)
			#data=json.loads(response.text)
			#person.append(name)
			#gender=data['gender']
			#if n in person_list or gender !='null':
			#	fp.write('person,'+n+'\n')

			
			
	fp.write('\n')
	fp.close()
	file.close()
'''
for i in os.listdir(path1):
	file=open(path1+"/"+i)
	fp=open("concepts/"+i+".con","a+")
	for line in file:
		tokens = nltk.tokenize.word_tokenize(line)
		tags = st.tag(tokens)
		for tag in tags:
			if tag[1]=='PERSON':
				fp.write('person,'+tag[0])
'''

pronoun_pos=['PRP','PRP$']

for i in os.listdir(path1):
	file=open(path1+"/"+i)
	fp=open("concepts/"+i+".con","a+")
	pronoun_list=[]
	person_list=[]
	for line in file:
			line=re.sub(r'[^\w]', ' ', line)
			tokenized = nltk.word_tokenize(line)
			tagged = nltk.pos_tag(tokenized)
			tsize = len(tagged)
			for j in range(0,tsize):
				if (tagged[j][1] == 'PRP$'):
					pronoun_list.append(tagged[j][0])
				if (tagged[j][1] == 'PRP'):
					person_list.append(tagged[j][0])
			for p in pronoun_list:
				fp.write('pronoun,'+p+'\n')
			for p in person_list:
				fp.write('person,'+p+'\n')
	fp.close()
	file.close()



'''
for i in os.listdir(path1):
	file=open(path1+"/"+i)
	fp=open("concepts/"+i+".con","a+")
	for line in file:
		tokens = nltk.tokenize.word_tokenize(line)
		tags = st.tag(tokens)
		for tag in tags:
			if tag[1]=='PERSON': 
				fp.write('person'+tag[0]+'\n')
'''








	





