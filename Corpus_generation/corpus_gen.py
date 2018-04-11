import nltk
from nltk.corpus import stopwords
import sys
from os import listdir
from os.path import isfile, join
import pickle

## Give command line arguments for your dataset directory path.

directory_path1 = sys.argv[1] #First directory 
onlyfiles = [f for f in listdir(directory_path1) if isfile(join(directory_path1, f))] # Lists all the files in the directory

corpus = []
for files in onlyfiles:
	filename = directory_path1 + '/' + files
	with open(filename) as f:
		for line in f:
			tokens = nltk.word_tokenize(line)
			corpus.append(tokens)

directory_path2 = sys.argv[2] #Second directory 
onlyfiles1 = [f for f in listdir(directory_path2) if isfile(join(directory_path2, f))] # Lists all the files in the directory
for files in onlyfiles1:
	filename = directory_path2 + '/' + files
	with open(filename) as f:
		for line in f:
			tokens = nltk.word_tokenize(line)
			corpus.append(tokens)
			
			
			
#mimic data corpus generation
directory_path3 = sys.argv[3] #third directory for mimic data
onlyfiles2 = [f for f in listdir(directory_path3) if isfile(join(directory_path3, f))] # Lists all the files in the directory
for files in onlyfiles2:
    filename = directory_path3 + '/' + files
    with open(filename) as f:
        for line in f:
            token = nltk.word_tokenize(line)
            corpus.append(tokens)
            
pickle.dump(corpus, open( "corpus.pkl", "wb" ),protocol=2)