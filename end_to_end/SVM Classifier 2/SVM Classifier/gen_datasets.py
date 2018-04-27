import sys
import pickle
import numpy as np
from sklearn.model_selection import train_test_split

path = sys.argv[1]

def splitdata(path):
    f = open(path,"r+")
    featuresets=[]
    X =[]
    Y = []
    for line in f:
    	vect = []
        if (line.strip() == "|"):
            continue
        else:
            s=line.strip().split("|")
            
            y1 = s[-1].strip()
            
            Y.append(int(y1))
            
            for i in range(0,23):
                vect.append(float(s[i].strip()))
            X.append(vect)
    
    print "Splitting data random"
    X, x_test, y, y_test = train_test_split(np.asarray(X), np.asarray(Y), test_size=0.20, random_state=None)

    pickle.dump(x_test, open( "X.pkl", "wb" ),protocol=2)
    pickle.dump(y_test, open( "Y.pkl", "wb" ),protocol=2)
    print "pickle generated"
    #print X[:30]
    #print Y

splitdata(path)