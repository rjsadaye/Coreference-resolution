import keras
from keras import backend as K
import tensorflow as tf
import sys
import numpy as np
from keras.models import Sequential,Model
from keras.layers import Dense, Input, Activation,Flatten,Dropout
from keras.utils import plot_model
from keras.optimizers import SGD, adam
from sklearn.model_selection import train_test_split
from keras.models import load_model
from keras.models import model_from_json


with open('model_architecture.json', 'r') as f:
    model = model_from_json(f.read())

model.load_weights('model_weights.h5')
print model.summary


path = sys.argv[1]
def splitdata(path):
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

    print len(X)
    print len(Y)
    
    return X
'''
CODE TO PASS INPUT TO THE MODEL
input should be vector of phrases
into x_test

I should have an phrase.txt for the corresponding input file 
structure of the phrase.txt file: Phrase || line:column
'''
x_test = splitdata(path) #
prediction = model.predict_classes(np.asarray(x_test))
prediction_list = prediction.tolist()
print prediction_list
print len(prediction_list)
f2 = open("classify_output.txt","w")
i = 0
path2 = sys.argv[2]
with open(path2) as f1:
	for line in f1:
		f2.write(line.split("\n")[0] + "|" + str(prediction_list[i]) + "\n")
		i += 1
