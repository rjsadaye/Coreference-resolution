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

'''
CODE TO PASS INPUT TO THE MODEL
input should be vector of phrases
into x_test

I should have an phrase.txt for the corresponding input file 
structure of the phrase.txt file: Phrase || line:column
'''

prediction = model.predict_classes(x_test)
predcition_list = prediction.tolist()

f2 = open("classify_output.txt")
with open(path) as f1:
	for line in f1 and i in range(len(predcition_list)):
		f2.write(line.split("\n")[0] + "||" + predcition_list[i] + "\n")
