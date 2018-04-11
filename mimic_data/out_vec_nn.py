import os
import sys

# Represents concepts as numerical values
path = "output_mimic.txt"
f2 = open("output_vector.txt","w+")
with open(path) as f1:
	for line in f1:
		if (line.split("\n")[0] == "person"):
			f2.write("1"+"\n")
		elif(line.split("\n")[0] == "pronoun"):
			f2.write("0"+"\n")
		elif(line.split("\n")[0] == "test"):
			f2.write("2"+"\n")
		elif(line.split("\n")[0] == "treatment"):
			f2.write("3"+"\n")
		elif(line.split("\n")[0] == "problem"):
			f2.write("4"+"\n")
	

f1.close()
f2.close()

# Generates the phrase and class pairs file
path1 = "input_mimic.txt"
path2 = "output_vector.txt"
f3 = open("phrase_class_dict.txt","w+")
with open(path1) as f1, open(path2) as f2:
	for l1, l2 in zip(f1, f2):
		temp1 = l1.split("\n")[0]
		temp2 = l2.split("\n")[0]

		f3.write(temp1.split("|")[0] + "|" + temp2 + "\n")
	

f1.close()
f2.close()
f3.close()

# Generates input and output pairs which will be used in a classifier
path1= sys.argv[1]
path2 = "phrase_class_dict.txt"
f3 = open("nn_input.txt","w+")
with open(path2) as f1, open(path1) as f2:
	for l1, l2 in zip(f1, f2):
		vector = l2.split(",")[:50]
		v1 = l1.split("|")[-1]
		vector = vector + list(v1)
		vector = ','.join(vector)
		#vector = ','.join(v1)
		f3.write(vector)

f1.close()
f2.close()
f3.close()
