import re
import sys
path=sys.argv[1]
#f1=open("/home/raj/end_to_end/output/mention_pairs/mention_pairs_clinical-1.txt","r")
f1=open(path)
f2=open("/home/raj/end_to_end/output/coreferent_pairs/output2.txt","a")

for line in f1:
	s=line.strip().split("|")
	if s[-1]=="0":
		continue
	if s[-1]=="1" or s[-1]==1:
		continue
	s1=s[0]
	s2=s[2]
	se1=s[1].split(" ")
	se2=s[3].split(" ")
	s1=re.sub(r'[^\w]', ' ', s1)
	s2=re.sub(r'[^\w]', ' ', s2)
	l1=s1.split(" ")
	l2=s2.split(" ")
	common=list(set(l1).intersection(l2))
	if len(common) !=0:
		f2.write(s1+"|"+se1[0]+"|"+se1[1]+"|"+s2+"|"+se2[0]+"|"+se2[1]+"|"+s[-1]+"\n")

f2.close()
