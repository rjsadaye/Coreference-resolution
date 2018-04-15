import pickle

with open('exact_name_l1.pickle','rb') as p:
	exact_name_l1=pickle.load(p)
with open('exact_name_l2.pickle','rb') as p:
	exact_name_l2=pickle.load(p)

with open('approximate_name_l1.pickle','rb') as p:
	approximate_name_l1=pickle.load(p)
with open('approximate_name_l2.pickle','rb') as p:
	approximate_name_l2=pickle.load(p)

with open('leftTruncation_name_l1.pickle','rb') as p:
	leftTruncation_name_l1=pickle.load(p)
with open('leftTruncation_name_l2.pickle','rb') as p:
	leftTruncation_name_l2=pickle.load(p)

with open('rightTruncation_name_l1.pickle','rb') as p:
	rightTruncation_name_l1=pickle.load(p)
with open('rightTruncation_name_l2.pickle','rb') as p:
	rightTruncation_name_l2=pickle.load(p)

with open('word_name_l1.pickle','rb') as p:
	word_name_l1=pickle.load(p)
with open('word_name_l2.pickle','rb') as p:
	word_name_l2=pickle.load(p)

with open('normalizedString_name_l1.pickle','rb') as p:
	normalizedString_name_l1=pickle.load(p)
with open('normalizedString_name_l2.pickle','rb') as p:
	normalizedString_name_l2=pickle.load(p)


def three_features(name_l1,name_l2):
	num_common_names=0

	num_common_names=len(set(exact_name_l1) & set(name_l2))	#Intersection of name results
	len_n1=len(name_l1)									#length of first name array
	len_n2=len(name_l2)									#length of second name array
