import os
import sys

# Represents concepts as numerical values

f2 = open("output_vector.txt","w+")
with open("output.txt") as f1:
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