import os
import subprocess

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
	