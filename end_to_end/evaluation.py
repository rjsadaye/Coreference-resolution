import sys

pathk=sys.argv[1] #Path to the system generated chain file
pathr=sys.argv[2] #Path to the gold mention chain file

def get_string_system(line):
	s=line.strip().split("|")
	n_concepts=(len(s)-1)
	i=0
	string1=""
	while(i<n_concepts):
		string1=string1+s[i]+" "
		i=i+2

	return string1


def get_string_gold(line):
	s=line.strip().split("||")
	n_concepts=len(s)-1
	string2=""
	for i in range(0,n_concepts):
		string2=string2+s[i].split("\"")[1]+" "
	return string2

def compute_similarity(string1,string2):
	a1=string1.strip().split(" ")
	a2=string2.strip().split(" ")
	count=0
	phikk=len(a1)
	phirr=len(a2)
	for key in a1:
		for val in a2:
			if(key==val):
				count=count+1
				a2.remove(val)
				break
	return count,phikk,phirr


fk=open(pathk,"r")
fr=open(pathr,"r")

precision_array=[]
recall_array=[]
f_measure_array=[]

s1=[]
s2=[]
for line in fk:
	string1=get_string_system(line)
	s1.append(string1)
for line in fr:
	string2=get_string_gold(line)
	s2.append(string2)
#print s1
#print s2

for i in s1:
	maxi=0
	phikk=1
	phirr=1
	#string1=get_string_system(line)
	for j in s2:
		#string2=get_string_gold(line2)
		n_max,n_phikk,n_phirr=compute_similarity(i,j)
		if(n_max>maxi):
			maxi=n_max
			phikk=n_phikk
			phirr=n_phirr
			#print maxi
			#print phikk
			#print phirr
	try:
		precision=float(maxi)/float(phirr)
		recall=float(maxi)/float(phikk)
		f_measure=(2*precision*recall)/(precision+recall)
		precision_array.append(precision)
		recall_array.append(recall)
		f_measure_array.append(f_measure)
	except:
		precision=0
		recall=0
		f_measure=0
		precision_array.append(precision)
		recall_array.append(recall)
		f_measure_array.append(f_measure)


print "precision="+str(sum(precision_array)/len(precision_array))
print "recall="+str(sum(recall_array)/len(recall_array))
print "f_measure="+str(sum(f_measure_array)/len(f_measure_array))
		


#print get_string_system("physical therapy|107:17 107:18|Xalatan|122:1 122:1|Prednisone|121:1 121:1|respiratory therapy|113:10 113:11|continued respiratory therapy|113:9 113:11|3")
#print get_string_gold("c=\"severe chronic obstructive pulmonary disease\" 21:0 21:4||c=\"severe chronic obstructive pulmonary disease\" 30:9 30:13||c=\"his usual severe bilateral emphysema_____\" 48:20 48:24||c=\"severe chronic obstructive pulmonary disease\" 112:15 112:19||t=\"coref problem\"")