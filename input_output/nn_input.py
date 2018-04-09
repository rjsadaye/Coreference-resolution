import sys

# Generates input and output pairs which will be used in a classifier
path1= sys.argv[1]
path2 = sys.argv[2]
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
