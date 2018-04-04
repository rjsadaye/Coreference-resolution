#import tf_glove
import os
import sys
import pickle

#pickle_path=sys.argv[1]

#with open(pickle_path) as f:
#	corpus = pickle.load(f)

path = sys.argv[1]

#model = tf_glove.GloVeModel(embedding_size=20, context_size=1)
#model.fit_to_corpus(corpus)
#model.train(num_epochs=100)

f1=open("input.txt","w+")
f2=open("output.txt","w+")
for i in os.listdir(path):
	if i.endswith('.txt.con'):
		file = open(path+"/"+i, 'r')
		vector=[0]*20
		for line in file:
			s=line.split("\"")
			f1.write(s[1]+"\n")
			f2.write(s[3]+"\n")

f1.close()
f2.close()


