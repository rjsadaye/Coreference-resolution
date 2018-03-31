import tf_glove
file = open('pfile.txt', 'r')
phrases=[] 
for line in file:
	phrases.append(line) 

model = tf_glove.GloVeModel(embedding_size=300, context_size=10)
model.fit_to_corpus(clinical-1)
model.train(num_epochs=100)

embed=[]
for p in phrases:
	embed.append(model.embedding_for(p))

print(embed[0])

