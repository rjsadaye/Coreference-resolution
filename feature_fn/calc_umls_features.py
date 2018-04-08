import pickle

with open('name_l1.pickle','rb') as p:
	name_l1=pickle.load(p)
with open('name_l2.pickle','rb') as p:
	name_l2=pickle.load(p)

num_common_names=0

num_common_names=len(set(name_l1) & set(name_l2))	#Intersection of name results
len_n1=len(name_l1)									#length of first name array
len_n2=len(name_l2)									#length of second name array
