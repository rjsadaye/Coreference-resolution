import tf_glove
import os
import sys
import pickle

pickle_path=sys.argv[1]

with open(pickle_path) as f:
	corpus = pickle.load(f)

path=sys.argv[2]

model = tf_glove.GloVeModel(embedding_size=20, context_size=1)
model.fit_to_corpus(corpus)
model.train(num_epochs=100)

embed=[]
file = open(path, 'r')
vector=[0]*20
for line in file:
	line=line.strip("\n")
	s=line.split(" ")
	count=0
	for si in s:
		if(si=='\n'):
			continue
		try:
			vector+=model.embedding_for(si)
			count+=1
		except Exception as e:
			print e
			continue
		if(count==0):
			continue
		vector=vector/count
		embed.append(vector)
				

			#phrases.append(line) 
		#for p in phrases:
			

gfile=open("path.glove","w+")
for item in embed:
    gfile.write("%s\n"%item)

        #gfile.close()

		#print(embed[0])

