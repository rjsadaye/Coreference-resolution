#import tf_glove
import os
import sys
import pickle
import subprocess
import re
import math


#pickle_path=sys.argv[1] #path to corpus.pkl file

pairs_path=sys.argv[1]	#path to pairs folder

output_path=sys.argv[2]	#path where output folder 
'''
with open(pickle_path) as f:
	corpus = pickle.load(f)
'''
#path=sys.argv[2]

#data = sys.argv[3]
'''
model = tf_glove.GloVeModel(embedding_size=30, context_size=1)
model.fit_to_corpus(corpus)
model.train(num_epochs=100)
'''

def glove_vector(c1,c2):
	
	vector1=[0]*30
	c1=re.sub(r'[^\w]', ' ', c1)
	c2=re.sub(r'[^\w]', ' ', c2)
	for si in c1:
		vector1+=model.embedding_for(si)
	vector2=[0]*30
	for si in c2:
		vector2+=model.embedding_for(si)
	return vector1+vector2

def longestSubstringFinder(string1, string2):
    answer = ""
    len1, len2 = len(string1), len(string2)
    for i in range(len1):
        match = ""
        for j in range(len2):
            if (i + j < len1 and string1[i + j] == string2[j]):
                match += string2[j]
            else:
                if (len(match) > len(answer)): answer = match
                match = ""
    return answer

def doeslastmatch(string1,string2):	#Checks if last word matches
	s1=re.sub(r'[^\w]', ' ', string1)	#Removing symbols from string
	s2=re.sub(r'[^\w]', ' ', string2)	
	s1=string1.split(" ")
	s2=string1.split(" ")
	if s1[-1]==s2[-1]:
		return 1
	else:
		return 0

def doesfirstmatch(string1,string2): #Checks if first word matches
	s1=re.sub(r'[^\w]', ' ', string1)	#Removing symbols from string
	s2=re.sub(r'[^\w]', ' ', string2)
	s1=string1.split(" ")
	s2=string1.split(" ")
	if s1[-1]==s2[-1]:
		return 1
	else:
		return 0

ctypedict={'coref pronoun': 0, 'coref person':1,'coref treatment':2,'coref problem':3,'coref test':4,'null':5}
def num_words_concept(string1):
	s1=re.sub(r'[^\w]', ' ', string1)
	words=s1.split(" ")
	return len(words)


for i in os.listdir(pairs_path):
	print i
	f=open(pairs_path+"/"+i,'r')
	if os.stat(pairs_path+"/"+i).st_size == 0:
		continue
	fp=open(output_path+'/feature'+i,'w+')
	for line in f:
		feature_vector=[]
		pipe=line.split("|")
		if pipe[-2]=="5":
			continue
		c1=pipe[0]
		c2=pipe[2]
		ctype=pipe[4]
		c1line=pipe[1].split(" ")
		c2line=pipe[3].split(" ")
		c1ls=c1line[0].split(":")
		c2ls=c2line[0].split(":")
		c1le=c1line[1].split(":")
		c2le=c2line[1].split(":")
		#feature_vector=feature_vector+glove_vector(c1,c2)
		common=longestSubstringFinder(c1,c2)
		len_common=len(common)					#Length of longest common substring of each concept
		max_mention_length=max(len(c1),len(c2))	#Which of the concept mention is longer in length
		part_common=max_mention_length-len_common
		feature_vector.append(float(ctype))
		feature_vector.append(len_common)
		feature_vector.append(part_common)
		feature_vector.append(doesfirstmatch(c1,c2))
		feature_vector.append(doeslastmatch(c1,c2))
		feature_vector.append(len(c1))
		feature_vector.append(len(c2))
		feature_vector.append(num_words_concept(c1))
		feature_vector.append(num_words_concept(c2))
		feature_vector.append(float(c1ls[0]))
		feature_vector.append(float(c1ls[1]))
		feature_vector.append(float(c1le[0]))
		feature_vector.append(float(c1le[1]))
		feature_vector.append(float(c2ls[0]))
		feature_vector.append(float(c2ls[1]))
		feature_vector.append(float(c2le[0]))
		feature_vector.append(float(c2le[1]))
		feature_vector.append(abs(float(c1ls[0])-float(c2ls[0])))
		words_common=re.sub(r'[^\w]', ' ', common)
		feature_vector.append(len(words_common))
		feature_vector.append(num_words_concept(words_common))
		lf=(float((num_words_concept(words_common)+1))/float((num_words_concept(c1)+num_words_concept(c2))))
		feature_vector.append(float(num_words_concept(c1))/(float(num_words_concept(c1)+num_words_concept(c2))))
		#feature_vector.append(math.log(lf))
		if(c1==c2):
			feature_vector.append(1)
		else:
			feature_vector.append(0)		
		feature_vector.append(lf)		
		feature_vector.append(c1)
		feature_vector.append(c1line[0])
		feature_vector.append(c1line[1])
		feature_vector.append(c2)
		feature_vector.append(c2line[0])
		feature_vector.append(c2line[1])
		#feature_vector.append(pipe[-1])
		for feature in feature_vector:
			fp.write("%s|" % feature)
		fp.write('\n')
	fp.close()
	f.close()





'''
embed=[]
embedstr			fp.write("%s," % feature)ing=[]
file = open(path, 'r')
vector=[0]*50
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
		#vector=vector/count
		embed.append(vector)
		embedstring.append(line)		

			#phrases.append(line) 
		#for p in phrases:
			

gfile=open(data+"path.glove","w")
for j in range(0,len(embed)):
	for i in embed[j]:
		gfile.write("%s,"%i)

	gfile.write(embedstring[j]+"\n")


        #gfile.close()

		#print(embed[0])

'''
