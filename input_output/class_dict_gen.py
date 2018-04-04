import os
import sys

# Generates the phrase and class pairs file
f3 = open("phrase_class_dict.txt","w+")
with open("input.txt") as f1, open("output_vector.txt") as f2:
	for l1, l2 in zip(f1, f2):
		f3.write(l1.split("\n")[0] + "," + l2.split("\n")[0] + "\n")
	

f1.close()
f2.close()
f3.close()

