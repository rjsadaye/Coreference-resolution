from sklearn import svm
import pickle
import numpy as np
from sklearn.model_selection import train_test_split
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.metrics import precision_recall_fscore_support
from sklearn.svm import SVC,LinearSVC,NuSVC
from nltk.classify import ClassifierI


with open("X.pkl") as f1:
	X = pickle.load(f1)
with open("Y.pkl") as f2:
	Y = pickle.load(f2)
print "Splitting data random"

X, x_test, y, y_test = train_test_split(X, Y, test_size=0.33, random_state=None)
print "Splitting data random"
print X.shape
print y.shape
print y_test
unique, counts = np.unique(y_test, return_counts=True)
print np.asarray((unique, counts)).T

#clf = svm.SVC(kernel='rbf',C = 1.0, gamma=1)
'''
clf = svm.SVC(kernel='rbf',C = 1.0,class_weight='balanced', gamma='auto')

clf.fit(X, y)  
clf.score(X, y)
save_classifier = open("svc.pickle","wb")
pickle.dump(clf, save_classifier,protocol=2)
save_classifier.close()
'''
#Predict Output

with open("svc.pickle") as f4:
	clf = pickle.load(f4)

y_pred = clf.predict(x_test)
print clf.score(x_test,y_test)
f3 = open("prediction.txt","w+")
for i in range(0,y_test.shape[0]):
	y1 = x_test[i].tolist()
	#print y1
	y1 = ','.join(str(v) for v in y1)

	f3.write(y1)
	f3.write(",")
	
	y2 = y_pred[i].tolist()
	#y2 = ''.join(str(v) for v in y2)
	f3.write(str(y2))
	f3.write("\n")
	

result1 = precision_recall_fscore_support(y_test, y_pred, average='binary')
print result1
result2 = precision_recall_fscore_support(y_test, y_pred, average='micro')
print result2
result3 = precision_recall_fscore_support(y_test, y_pred, average='weighted')
print result3


y_pred = clf.predict([[0.0,0,3,1,1,3,3,1,1,109.0,34.0,109.0,34.0,109.0,0.0,109.0,0.0,0.0,0,1,0.5,0.0,1.0]])
print y_pred