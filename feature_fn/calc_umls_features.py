import pickle

with open('exact_name_l1.pickle','rb') as p:
	exact_name_l1=pickle.load(p)
with open('exact_name_l2.pickle','rb') as p:
	exact_name_l2=pickle.load(p)

num_common_names=0

exact_num_common_names=len(set(exact_name_l1) & set(name_l2))	#Intersection of name results
exact_len_n1=len(name_l1)									#length of first name array
exact_len_n2=len(name_l2)									#length of second name array
