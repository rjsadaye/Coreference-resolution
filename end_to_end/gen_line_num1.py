import sys
import os
import re
path1 = sys.argv[1] # path to docs folder containing the clamp-out and final-concepts empty folder
path2 = sys.argv[2] # path to clamp output

sem_string = "semantic"

def findOccurrences(temp,phrase,o):
	temp = temp.split()
	positions = []
	phrase = phrase.split()

	if(len(phrase) == 1):
		if(len(o) == 1 ):
			#print "IN IF"
			indices = [i for i, x in enumerate(temp) if x == phrase[0]]
			positions.append([indices[0],indices[0]])
		else:
			indices = [i for i, x in enumerate(temp) if x == phrase[0]]
			for ind in indices:
				start,end = ind
				positions.append([start,end])
	else:
		# if(len(o) == 1):
		# 	start = temp.index(phrase[0])
		# 	end = temp.index(phrase[-1])
		# 	positions.append([start,end])
		# else:
		startindices = [i for i, x in enumerate(temp) if x == phrase[0]]
		endindices = [i for i, x in enumerate(temp) if x == phrase[-1]]
		#print startindices
		#print endindices
		for s in startindices:
			for e in endindices:
				# print (e-s)
				# print len(phrase)
				if((e-s) == len(phrase)-1):

					start,end = s,e
					positions.append([start,end])
				

	return positions

for i in os.listdir(path1):
	if i.endswith("txt"):
		print str(i) + " is being processed"
		doc = open(path1+"/"+str(i))
		clamp = open(path2+"/"+str(i))
		clamp_concept=[]
		outfile = open(path1 + "/final_concepts/"+str(i).split(".")[0]+".txt","w+")
		for concept_line in clamp:
			num = 1
			if sem_string in concept_line:
				line_list = concept_line.strip().split("\t")
				semantic = line_list[3].split("=")
				ne = line_list[5].split("=")
				#print ne
				clamp_concept.append([ne[1],semantic[1]])
		#print clamp_concept		
		
		for (line_num, line) in enumerate(doc):
			line_list = line.strip()
			temp = line_list
			for concept in clamp_concept:
				
				# if(len(o)!=0):
				# 	print "all occurences:	" 
				# 	print o
				try:
					o = re.findall(r'\b'+ str(concept[0]) +r'\b',temp)
					if (re.search(r'\b'+ str(concept[0]) +r'\b',temp)):
						phrase = concept[0]
						print temp
						print phrase
						positions = findOccurrences(temp,phrase,o)
						print positions
						for p in positions:
							outfile.write(concept[0]+"|"+str(line_num+1)+ ":" + str(p[0]) +" " + str(line_num+1) + ":" + str(p[1]) +"|" +concept[1]+"\n")
				except:
					pass
	#uniqlines = outfile.readlines()

	#outfile.writelines(set(uniqlines))

			
