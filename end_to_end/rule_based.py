
from __future__ import print_function
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
from sutime import SUTime


import os
import pickle
from argparse import ArgumentParser
from platform import system
from subprocess import Popen
from sys import argv
from sys import stderr
import shlex
from subprocess import Popen, PIPE,STDOUT


### SAMPLE COMMAND:
### python rule_based.py /home/raj/nlp_data/Partners_Train/docs /home/raj/Coreference-resolution/rule_based_concepts/clamp_out  /home/raj/Downloads/python-sutime-master/jars 

path1 =sys.argv[1] #path to the docs folder

path2=sys.argv[2]   #path to the clamp output  folder

path3=sys.argv[3]	#path to the jars folder in SU-Time master folder

IS_WINDOWS = True if system() == 'Windows' else False
JAVA_BIN_PATH = 'java.exe' if IS_WINDOWS else 'java'
STANFORD_NER_FOLDER = 'stanford-ner'
#ner=[]


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

def arg_parse():
	arg_p = ArgumentParser('Stanford NER Python Wrapper')
	arg_p.add_argument('-f', '--filename', type=str, default=None)
	arg_p.add_argument('-v', '--verbose', action='store_true')
	return arg_p


def debug_print(log, verbose):
	if verbose:
		print(log)


def process_entity_relations(entity_relations_str, verbose=True):
	# format is ollie.
	entity_relations = list()
	for s in entity_relations_str:
		entity_relations.append(s[s.find("(") + 1:s.find(")")].split(';'))
	return entity_relations


def stanford_ner(filename, verbose=True, absolute_path=None):
	out = 'out.txt'

	command = ''
	if absolute_path is not None:
		command = 'cd {};'.format(absolute_path)
	else:
		filename = '../{}'.format(filename)

	command += 'cd {}; {} -mx1g -cp "*:lib/*" edu.stanford.nlp.ie.NERClassifierCombiner ' \
			   '-ner.model classifiers/english.all.3class.distsim.crf.ser.gz ' \
			   '-outputFormat tabbedEntities -textFile {} > ../{}' \
		.format(STANFORD_NER_FOLDER, JAVA_BIN_PATH, filename, out)

	if verbose:
		debug_print('Executing command = {}'.format(command), verbose)
		java_process = Popen(command, stdout=stderr, shell=True)
	else:
		java_process = Popen(command, stdout=stderr, stderr=open(os.devnull, 'w'), shell=True)
	java_process.wait()
	assert not java_process.returncode, 'ERROR: Call to stanford_ner exited with a non-zero code status.'

	if absolute_path is not None:
		out = absolute_path + out

	with open(out, 'r') as output_file:
		results_str = output_file.readlines()
	os.remove(out)

	results = []
	for res in results_str:
		if len(res.strip()) > 0:
			split_res = res.split('\t')
			entity_name = split_res[0]
			entity_type = split_res[1]

			if len(entity_name) > 0 and len(entity_type) > 0:
				results.append([entity_name.strip(), entity_type.strip()])

	if verbose:
		pickle.dump(results_str, open('out.pkl', 'wb'))
		debug_print('wrote to out.pkl', verbose)
	return results


def main(args):
	ner=[]
	#arg_p = arg_parse().parse_args(args[1:])
	#filename = arg_p.filename
	filename=args
	#verbose = args.verbose
	#debug_print(arg_p, verbose)
	if filename is None:
		print('please provide a text file containing your input. Program will exit.')
		exit(1)
	#if verbose:
		#debug_print('filename = {}'.format(filename), verbose)
	#entities = stanford_ner(filename, verbose)
	entities = stanford_ner(filename)
	#print('\n'.join([entity[0].ljust(20) + ',' + entity[1] for entity in entities]))
	for entity in entities:
		if(entity[1]=='PERSON'):
			ner.append(entity[0])
	return ner


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




subprocess.call(['/home/raj/end_to_end/ClampCmd_1.4.0/run_ner_pipeline.sh',path1,'clamp_out'])

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
	if i.endswith("txt"):
		print (str(i) + " is being processed")
		file=open(path1+"/"+i)
		fp=open("concepts/"+i+".con","a+")
		num = 1
		for line in file:
			
			noun_list=get_noun_phrases(line)
			for n in noun_list:
				if n in person_list:
					#words = n.split()
					line_list = line.split()
					#print (words)
					print (line_list)
					if (n not in line_list):
						regex = re.compile(r"\b"+n+"\b",re.IGNORECASE)
						print (regex)
						if(n in ll.lower() for ll in line_list):
							if (regex.search(str(n))):
								line_list = line.lower().split()
								start = line_list.index(n)
								end = line_list.index(n)
						else:
							continue
					else:
						start = line_list.index(n)
						end = line_list.index(n)
						fp.write(n+"|"+str(num)+":" +str(start) + " "+str(num) +":" +str(end) +"|person"+"\n")
			num += 1

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
	if i.endswith("txt"):
		file=open(path1+"/"+i)
		fp=open("concepts/"+i+".con","a+")
		print(path1+"/"+i)
		ner=main(path1+"/"+i)
		
		#omp_cmd="python main.py -f %s -v" %(i)	
		#subprocess.call(["python main.py","-f",i,"-v"])
		#xmlResult = Popen(shlex.split(omp_cmd), stdout=PIPE, stderr=STDOUT)
		#with (open("ner.pkl", "rb")) as p:
		#	ner=pickle.load(p)
		num = 1
		for line in file:
			
			for n in ner:
				line_list = line.split()
				#print (line_list)
				if n in line_list:
					print ("*"*40)
					pp = n.split()
					print (pp)
					if (len(pp) == 1):
						indices = [i for i, x in enumerate(line_list) if x == str(pp[0])]
						for ind in indices:
							fp.write(n+"|"+str(num)+":" +str(ind) + " "+str(num) +":" +str(ind) +"|person"+"\n")
					else:
						start = line_list.index(str(pp[0]))
						end = line_list.index(str(pp[-1]))
						fp.write(n+"|"+str(num)+":" +str(start) + " "+str(num) +":" +str(end) +"|person"+"\n")
			num += 1
				
		fp.close()
		file.close()

for i in os.listdir(path1):
	if i.endswith("txt"):
		file=open(path1+"/"+i)
		fp=open("concepts/"+i+".con","a+")
		pronoun_list=[]
		person_list=[]
		num = 1
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
				line_list = line.split()
				#print (line_list)
				#if (p not in line_list):
					#regex = re.compile(r"\b"+n+"\b",re.IGNORECASE)
					#print (regex)
				#if(p in ll.lower() for ll in line_list):
					#if (regex.search(str(n))):
				#line_list = line.lower().split()
				print (line_list)
				print (p)
				if (p in line_list):
					print ("*"*40)
					pp = p.split()
					print (pp)
					indices = [i for i, x in enumerate(line_list) if x == str(pp[0])]
					start = line_list.index(str(pp[0]))
					end = line_list.index(str(pp[-1]))
				'''
				else:
					start = line_list.index(p)
					end = line_list.index(p)
					'''
				for ind in indices:
					fp.write(p+"|"+str(num)+":" +str(ind) + " "+str(num) +":" +str(ind) +"|pronoun"+"\n")
				#fp.write('pronoun,'+p+'\n')
			for p in person_list:
				line_list = line.split()
				#print (line_list)
				#if (p not in line_list):
					#regex = re.compile(r"\b"+n+"\b",re.IGNORECASE)
					#print (regex)
				#if(p in ll.lower() for ll in line_list):
					#if (regex.search(str(n))):
					#print (line_list)
				#line_list = line.lower().split()
				print (line_list)
				print (p)
				if p in line_list:
					print ("*"*40)
					pp = p.split()
					print (pp)
					if (len(pp) == 1):
						indices = [i for i, x in enumerate(line_list) if x == str(pp[0])]
						for ind in indices:
							fp.write(p+"|"+str(num)+":" +str(ind) + " "+str(num) +":" +str(ind) +"|person"+"\n")
					else:
						start = line_list.index(str(pp[0]))
						end = line_list.index(str(pp[-1]))
						fp.write(p+"|"+str(num)+":" +str(start) + " "+str(num) +":" +str(end) +"|person"+"\n")
					
				'''
				else:
					
					start = line_list.index(p)
					end = line_list.index(p)
					'''
				
				#fp.write('person,'+p+'\n')
			num += 1
		fp.close()
		file.close()
'''
jar_files = os.path.join(os.path.dirname(path3), 'jars')
sutime = SUTime(jars=jar_files, mark_time_ranges=True)

if __name__ == '__main__':
	for i in os.listdir(path1):
		if i.endswith("txt"):
			file=open(path1+"/"+i)
			fp=open("concepts/"+i+".con","a+")
			num = 1
			for line in file:
				
				data=json.dumps(sutime.parse(line))
				list_data=json.loads(data)
				for l in list_data:
					line_list = line.split()
				#print (line_list)
					#if (l not in line_list):
					#regex = re.compile(r"\b"+n+"\b",re.IGNORECASE)
					#print (regex)
					#if(l in ll.lower() for ll in line_list):
						#if (regex.search(str(n))):
					#line_list = line.lower().split()
					print (line_list)
					if (l["text"] in line_list):
						print ("*"*40)
						ll = l["text"].split()
						print (ll[0])
						print (ll[-1])
						start = line_list.index(str(ll[0]))
						end = line_list.index(str(ll[-1]))
					
						
						fp.write(l["text"]+"|"+str(num)+":" +str(start) + " "+str(num) +":" +str(end) +"|temporal"+"\n")
					#fp.write('temporal,'+l["text"]+'\n')
				num += 1
			fp.close()
			file.close()

'''
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








	





