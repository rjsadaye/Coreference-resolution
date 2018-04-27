import re
#f1 = open("/home/raj/end_to_end/feature_output/featuremention_pairs_clinical-1.txt","r+")
f2 = open("single_prediction.txt","r+")
f3 = open("output.txt","w+")
line_set = []
for line in f2:
	s = line.strip().split("|")
	if (s[-1] == '1'):
		f3.write(line)

'''
print "IN CLASSIFY_OUT"
print "TOTAL LINES:"
print len(line_set)
exit()
for line2 in f1:
	line2 = line2.strip()
	for line in line_set:
		temp = line
		line = '|'.join(str(v) for v in line[:-1])
		if (re.search(r'\b'+ str(line) +r'\b',line2)):
			concept = line2.split("|")
			
			#line = line.split(",")
			if(temp[-1] == '1'):
				f3.write('|'.join(str(v) for v in concept[23:])+"|")
				#f3.write(temp[-1]+"|")
				concept_type = float(temp[0])
				f3.write(str(int(concept_type))+"\n")
		else:
			continue
uniqlines = f3.readlines()

f3.writelines(set(uniqlines))
'''