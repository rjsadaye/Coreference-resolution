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
	len_common=len(common)
	