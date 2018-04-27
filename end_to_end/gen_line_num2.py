import sys
import os
path1 = sys.argv[1] # path to docs folder containing the clamp-out and final-concepts empty folder
path2 = sys.argv[2] # path to final concepts

person_string = "person"
pronoun_string = "pronoun"
temporal_string = "temporal"
pipe = "|"

for i in os.listdir(path1):
	if i.endswith("con"):
		print str(i) + " is being processed"
		person_pronoun = open(path1+"/"+str(i))
		file_name = str(i).split('.')
		#print file_name[0] + file_name[2]
		other = open(path2 + "/"+file_name[0]+"."+"txt","a")
		for person_line in person_pronoun:
			if(pipe in person_line):
				if (person_string in person_line):
					other.write(person_line.strip()+'\n')
			elif(pronoun_string in person_line):
				if(pipe in person_line):
					other.write(person_line.strip()+'\n')
			elif(temporal_string in person_line):
				if(pipe in person_line):
					other.write(person_line.strip()+'\n')

