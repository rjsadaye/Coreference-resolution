import sys
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report,confusion_matrix,accuracy_score,recall_score

path = sys.argv[1]
f = open(path,"r+")
featuresets=[]
X_train =[]
Y_train = []
for line in f:
    s=line.split(",")
    vect=[]
    for i in range(0,len(s)-2):
        vect.append(float(s[i]))
    #featuresets.append((vect,s[20]))
    X_train.append(vect)
    Y_train.append(list(s[20]))

train_X = X_train[:8000]
test_X = X_train[8000:]

train_Y = Y_train[:8000]
test_Y = Y_train[8000:]
'''
scaler = StandardScaler()
# Fit only to the training data
scaler.fit(X_train)

X_train = scaler.transform(train_X)
Y_train = scaler.transform(train_Y)
'''
mlp = MLPClassifier(hidden_layer_sizes=(100,100,100))
mlp.fit(X_train,Y_train)

predictions = mlp.predict(test_X)
score = mlp.score(test_X,test_Y)
recall = recall_score(test_Y,predictions,average = None)
print(recall)
print(score)
print(confusion_matrix(test_Y,predictions))
print(accuracy_score(test_Y,predictions))
#print(classification_report(tuple(test_Y),predictions))
