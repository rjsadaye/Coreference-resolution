import pickle
import sys

path = sys.argv[1]
f = open(path,"r+")
featuresets=[]
X =[]
Y = []
for line in f:
    s=line.split(",")
    vect = []
    vect2 =[]
    for i in range(0,len(s)-2):
        vect.append(float(s[i]))
    #featuresets.append((vect,s[20]))
    X.append(vect)
    if (s[50] == '0'):
    	vect2.append([1,0,0,0,0])
    elif(s[50] == '1'):
    	vect2.append([0,1,0,0,0])
    elif(s[50] == '2'):
    	vect2.append([0,0,1,0,0])
    elif(s[50] == '3'):
    	vect2.append([0,0,0,1,0])
    elif(s[50] == '4'):
    	vect2.append([0,0,0,0,1])
    Y = Y + vect2

pickle.dump(X, open( "X.pkl", "wb" ),protocol=2)
pickle.dump(Y, open( "Y.pkl", "wb" ),protocol=2)
print "pickle generated"