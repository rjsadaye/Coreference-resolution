from sklearn import svm
import pickle
import numpy as np
from sklearn import cross_validation
from sklearn.metrics import recall_score
from sklearn.model_selection import cross_validate,cross_val_predict
from sklearn.model_selection import train_test_split

from sklearn.metrics import precision_recall_fscore_support
from sklearn.svm import SVC,LinearSVC,NuSVC

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
scoring = ['precision_macro', 'recall_macro']
clf = svm.SVC(kernel='rbf',C = 1.0,class_weight='balanced', gamma='auto')
scores = cross_validate(clf, X, y, scoring=scoring,cv=10, return_train_score=False)
print scores['test_recall_macro']
print scores['test_precision_macro']
clf.fit(X, y)  
#clf.score(X, y)

save_classifier = open("svc.pickle","wb")
pickle.dump(clf, save_classifier,protocol=2)
save_classifier.close()

#Predict Output
'''
with open("svc.pickle") as f4:
	clf = pickle.load(f4)
'''
y_pred = cross_val_predict(clf, x_test, y_test, cv=10)
#y_pred = clf.predict(x_test)
print clf.score(y_test,y_pred)
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


y_pred = clf.predict([[2.0,0.0,7.0,1.0,1.0,6.0,7.0,1.0,2.0,82.0,0.0,82.0,0.0,84.0,4.0,84.0,5.0,2.0,0.0,1.0,0.333333333333,-0.405465108108,0.666666666667]])
print y_pred