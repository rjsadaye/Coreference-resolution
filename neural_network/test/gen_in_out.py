#import tf_glove
import os
import sys
import pickle

#pickle_path=sys.argv[1]

#with open(pickle_path) as f:
#	corpus = pickle.load(f)
'''
path1 = sys.argv[1] # Beth Train
path2 = sys.argv[2] # Partners Train

#model = tf_glove.GloVeModel(embedding_size=20, context_size=1)
#model.fit_to_corpus(corpus)
#model.train(num_epochs=100)

f1=open("input.txt","w+")
f2=open("output.txt","w+")
for i in os.listdir(path1):
	if i.endswith('.txt.con'):
		file = open(path1+"/"+i, 'r')
		for line in file:
			s=line.split("\"")
			f1.write(s[1]+"|"+ s[2].split("|")[0] + "\n")
			f2.write(s[3]+"\n")

for i in os.listdir(path2):
	if i.endswith('.txt.con'):
		file = open(path2+"/"+i, 'r')
		for line in file:
			s=line.split("\"")
			f1.write(s[1]+"|"+ s[2].split("|")[0] + "\n")
			f2.write(s[3]+"\n")

'''
path3 = sys.argv[1] # need to be changed later
f1=open("input.txt","w+")
f2=open("output.txt","w+")
f3 = open(path3)
for line in f3:
	s=line.split("\"")
	f1.write(s[1]+"|"+ s[2].split("||")[0] + "\n")
	f2.write(s[3]+"\n")

f1.close()
f2.close()
f3.close()

