import os
import subprocess
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

f=open('pairs file','r')

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

for line in f:
	s=line.split("|")
	c1=s[0]
	c2=s[3]
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

	