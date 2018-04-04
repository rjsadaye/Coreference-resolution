import sys

# Generates input and output pairs which will be used in a classifier
path = sys.argv[1]
f3 = open("nn_input.txt","w+")
with open("phrase_class_dict.txt") as f1, open(path) as f2:
	for l1, l2 in zip(f1, f2):
		vector = l2.split(",")[:20]
		vector.append(l1.split(",")[1])
		vector = ','.join(vector)
		f3.write(vector)

f1.close()
f2.close()
f3.close()