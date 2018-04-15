import os
import subprocess
import pickle
import sys
import re
import math
#Give input as path to folder contaiing pairs file
path=sys.argv[1]

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

def three_features(name_l1,name_l2):
	num_common_names=0

	num_common_names=len(set(name_l1) & set(name_l2))	#Intersection of name results
	len_n1=len(name_l1)									#length of first name array
	len_n2=len(name_l2)									#length of second name array
	return num_common_names,len_n1,len_n2


#f=open('pairs file','r')

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

for i in os.listdir(path):
	print i
	f=open(path+"/"+i,'r')
	fp=open('feature_folder/feature'+i,'w+')
	for line in f:
		feature_vector=[]
		s=line.split('\"')
		c1=str(s[1])
		c2=str(s[5])
		#print c1
		#print c2
		first_line=s[2].split(':')
		end_line=s[6].split(':')
		start_1, end_1=first_line[0],first_line[2]
		start_2,end_2=end_line[0],end_line[2]
		concept_type=ctypedict.get(s[3])
		#c1type=s[-1]
		#c2type=s[-2]
		'''
		try:
			os.remove('name_l1.pickle')
			os.remove('name_l2.pickle')
			os.remove('umls_results.pickle')
		except:
			print('does not exist')

		'''
		
		#with open('umls_results.pickle','rb') as p:
		#	umls_vector=pickle.load(p)
		common=longestSubstringFinder(c1,c2)
		len_common=len(common)					#Length of longest common substring of each concept
		max_mention_length=max(len(c1),len(c2))	#Which of the concept mention is longer in length
		part_common=max_mention_length-len_common

		if(c1==c2):	
			feature_vector.append(1)
		else:
			feature_vector.append(0)

		feature_vector.append(concept_type)	#concept type of the pair
		feature_vector.append(len_common)	#lengh of the common substring
		feature_vector.append(part_common)	#How much part is common in strings
		feature_vector.append(doesfirstmatch(c1,c2))	#does first word of the strings match
		feature_vector.append(doeslastmatch(c1,c2))		#does last word of the strings match
		feature_vector.append(len(c1))					#length of first concept string 
		feature_vector.append(len(c2))					#length of second concept string
		feature_vector.append(num_words_concept(c1))	#number of words in first concept string
		feature_vector.append(num_words_concept(c2))	#number of words in second concept string
		feature_vector.append(start_1)					#start of first concept
		feature_vector.append(start_2)					#start of second concept



		###Features of exact search
		subprocess.call(['./umls_concepts.sh',c1,c2,"exact"])

		with open('name_l1.pickle','rb') as p:
			name_l1=pickle.load(p)
		with open('name_l2.pickle','rb') as p:
			name_l2=pickle.load(p)
		f1,f2,f3=three_features(name_l1,name_l2)
		feature_vector.append(f1)				
		feature_vector.append(f2)
		feature_vector.append(f3)

		words_common=re.sub(r'[^\w]', ' ', common)
		feature_vector.append(len(words_common))	
		#ltf=math.log((len(words_common)+1)/(num_words_concept(c1)+num_words_concept(c2)+1))
		#feature_vector.append(ltf)
		for feature in feature_vector:
			fp.write("%s," % feature)
		fp.write(c1+",")
		fp.write(c2)
		fp.write("\n")
	fp.close()
	f.close()

'''
	###Features of word search
		subprocess.call(['./umls_concepts.sh',c1,c2,"words"])

		with open('name_l1.pickle','rb') as p:
			name_l1=pickle.load(p)
		with open('name_l2.pickle','rb') as p:
			name_l2=pickle.load(p)
		f1,f2,f3=three_features(name_l1,name_l2)
		feature_vector.append(f1)				
		feature_vector.append(f2)
		feature_vector.append(f3)
		
###Features of approximate search
		subprocess.call(['./umls_concepts.sh',c1,c2,"approximate"])

		with open('name_l1.pickle','rb') as p:
			name_l1=pickle.load(p)
		with open('name_l2.pickle','rb') as p:
			name_l2=pickle.load(p)
		f1,f2,f3=three_features(name_l1,name_l2)
		feature_vector.append(f1)				
		feature_vector.append(f2)
		feature_vector.append(f3)

###Features of  leftTruncation search
		subprocess.call(['./umls_concepts.sh',c1,c2,"leftTruncation"])

		with open('name_l1.pickle','rb') as p:
			name_l1=pickle.load(p)
		with open('name_l2.pickle','rb') as p:
			name_l2=pickle.load(p)
		f1,f2,f3=three_features(name_l1,name_l2)
		feature_vector.append(f1)				
		feature_vector.append(f2)
		feature_vector.append(f3)

###Features of  rightTruncation search
		subprocess.call(['./umls_concepts.sh',c1,c2,"rightTruncation"])

		with open('name_l1.pickle','rb') as p:
			name_l1=pickle.load(p)
		with open('name_l2.pickle','rb') as p:
			name_l2=pickle.load(p)
		f1,f2,f3=three_features(name_l1,name_l2)
		feature_vector.append(f1)				
		feature_vector.append(f2)
		feature_vector.append(f3)

###Features of  normalizedString search
		subprocess.call(['./umls_concepts.sh',c1,c2,"normalizedString"])

		with open('name_l1.pickle','rb') as p:
			name_l1=pickle.load(p)
		with open('name_l2.pickle','rb') as p:
			name_l2=pickle.load(p)
		f1,f2,f3=three_features(name_l1,name_l2)
		feature_vector.append(f1)				
		feature_vector.append(f2)
		feature_vector.append(f3)

'''


		#log term frequency
		










	