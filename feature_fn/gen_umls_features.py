import os
import subprocess
import pickle
import sys

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

def num_words_concept(string1):
	s1=re.sub(r'[^\w]', ' ', string1)
	words=s1.split(" ")
	return len(words)

for i in os.listdir(path):
	f=open(i,'r')
	fp=open('feature_folder/feature'+i,'w+')
	for line in f:
		feature_vector=[]
		s=line.split("|")
		c1=s[0]
		c2=s[3]
		start_1, end_1,start_2,end_2,concept_type=s[1],s[2],s[4],s[6]
		#c1type=s[-1]
		#c2type=s[-2]
		os.remove('name_l1.pickle')
		os.remove('name_l2.pickle')
		os.remove('umls_results.pickle')
		subprocess.call(['./umls_concepts.sh',c1,c2])
		with open('umls_results.pickle','rb') as p:
			umls_vector=pickle.load(p)
		common=longestSubstringFinder(c1,c2)
		len_common=len(common)					#Length of longest common substring of each concept
		max_mention_length=max(len(c1),len(c2))	#Which of the concept mention is longer in length
		part_common=max_mention_length-len_common


		feature_vector.append(concept_type)
		feature_vector.append(len_common)
		feature_vector.append(part_common)
		feature_vector.append(doesfirstmatch(c1,c2))
		feature_vector.append(doeslastmatch(c1,c2))
		feature_vector.append(len(c1))
		feature_vector.append(len(c2))
		feature_vector.append(num_words_concept(c1))
		feature_vector.append(num_words_concept(c2))
		feature_vector.append(start_1)
		feature_vector.append(start_2)

		with open('exact_name_l1.pickle','rb') as p:
		exact_name_l1=pickle.load(p)
		with open('exact_name_l2.pickle','rb') as p:
			exact_name_l2=pickle.load(p)

		with open('approximate_name_l1.pickle','rb') as p:
			approximate_name_l1=pickle.load(p)
		with open('approximate_name_l2.pickle','rb') as p:
			approximate_name_l2=pickle.load(p)

		with open('leftTruncation_name_l1.pickle','rb') as p:
			leftTruncation_name_l1=pickle.load(p)
		with open('leftTruncation_name_l2.pickle','rb') as p:
			leftTruncation_name_l2=pickle.load(p)

		with open('rightTruncation_name_l1.pickle','rb') as p:
			rightTruncation_name_l1=pickle.load(p)
		with open('rightTruncation_name_l2.pickle','rb') as p:
			rightTruncation_name_l2=pickle.load(p)

		with open('word_name_l1.pickle','rb') as p:
			word_name_l1=pickle.load(p)
		with open('word_name_l2.pickle','rb') as p:
			word_name_l2=pickle.load(p)

		with open('normalizedString_name_l1.pickle','rb') as p:
			normalizedString_name_l1=pickle.load(p)
		with open('normalizedString_name_l2.pickle','rb') as p:
			normalizedString_name_l2=pickle.load(p)
		
		f1,f2,f3=three_features(exact_name_l1,exact_name_l2)
		feature_vector.append(f1)
		feature_vector.append(f2)
		feature_vector.append(f3)
		
		f1,f2,f3=three_features(approximate_name_l1,approximate_name_l2)
		feature_vector.append(f1)
		feature_vector.append(f2)
		feature_vector.append(f3)

		f1,f2,f3=three_features(normalizedString_name_l1,normalizedString_name_l2)
		feature_vector.append(f1)
		feature_vector.append(f2)
		feature_vector.append(f3)

		f1,f2,f3=three_features(leftTruncation_name_l1,leftTruncation_name_l2)
		feature_vector.append(f1)
		feature_vector.append(f2)
		feature_vector.append(f3)

		f1,f2,f3=three_features(rightTruncation_name_l1,rightTruncation_name_l2)
		feature_vector.append(f1)
		feature_vector.append(f2)
		feature_vector.append(f3)

		f1,f2,f3=three_features(word_name_l1,word_name_l2)
		feature_vector.append(f1)
		feature_vector.append(f2)
		feature_vector.append(f3)

		#log term frequency
		words_common=re.sub(r'[^\w]', ' ', common)
		feature_vector.append(len(words_common))	
		ltf=Math.log((len(words_common)+1)/(num_words_concept(c1)+num_words_concept(c2)))
		feature_vector.append(ltf)
		for feature in feature_vector:
			fp.write("%s," % feature)
		fp.write(c1+",")
		fp.write(c2)
		fp.write("\n")
	fp.close()
	f.close()







def three_features(name_l1,name_l2):
	num_common_names=0

	num_common_names=len(set(exact_name_l1) & set(name_l2))	#Intersection of name results
	len_n1=len(name_l1)									#length of first name array
	len_n2=len(name_l2)									#length of second name array
	return num_common_names,len_n1,len_n2


	