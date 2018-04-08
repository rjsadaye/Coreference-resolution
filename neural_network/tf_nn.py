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


path = sys.argv[1]

def mcor(y_true, y_pred):
     #matthews_correlation
    y_pred_pos = K.round(K.clip(y_pred, 0, 1))
    y_pred_neg = 1 - y_pred_pos
 
 
    y_pos = K.round(K.clip(y_true, 0, 1))
    y_neg = 1 - y_pos
    tp = K.sum(y_pos * y_pred_pos)
    tn = K.sum(y_neg * y_pred_neg)
 
    fp = K.sum(y_neg * y_pred_pos)
    fn = K.sum(y_pos * y_pred_neg)
 
    numerator = (tp * tn - fp * fn)
    denominator = K.sqrt((tp + fp) * (tp + fn) * (tn + fp) * (tn + fn))
    return numerator / (denominator + K.epsilon())




def precision(y_true, y_pred):
    """Precision metric.

    Only computes a batch-wise average of precision.

    Computes the precision, a metric for multi-label classification of
    how many selected items are relevant.
    """
    true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
    predicted_positives = K.sum(K.round(K.clip(y_pred, 0, 1)))
    precision = true_positives / (predicted_positives + K.epsilon())
    return precision

def recall(y_true, y_pred):
    """Recall metric.

    Only computes a batch-wise average of recall.

    Computes the recall, a metric for multi-label classification of
    how many relevant items are selected.
    """
    true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
    possible_positives = K.sum(K.round(K.clip(y_true, 0, 1)))
    recall = true_positives / (possible_positives + K.epsilon())
    return recall

def f1(y_true, y_pred):
    def recall(y_true, y_pred):
        """Recall metric.

        Only computes a batch-wise average of recall.

        Computes the recall, a metric for multi-label classification of
        how many relevant items are selected.
        """
        true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
        possible_positives = K.sum(K.round(K.clip(y_true, 0, 1)))
        recall = true_positives / (possible_positives + K.epsilon())
        return recall

    def precision(y_true, y_pred):
        """Precision metric.

        Only computes a batch-wise average of precision.

        Computes the precision, a metric for multi-label classification of
        how many selected items are relevant.
        """
        true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
        predicted_positives = K.sum(K.round(K.clip(y_pred, 0, 1)))
        precision = true_positives / (predicted_positives + K.epsilon())
        return precision
    precision = precision(y_true, y_pred)
    recall = recall(y_true, y_pred)
    return 2*((precision*recall)/(precision+recall))

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
        if (s[20] == '0'):
        	vect2.append([1,0,0,0,0])
        elif(s[20] == '1'):
        	vect2.append([0,1,0,0,0])
        elif(s[20] == '2'):
        	vect2.append([0,0,1,0,0])
        elif(s[20] == '3'):
        	vect2.append([0,0,0,1,0])
        elif(s[20] == '4'):
        	vect2.append([0,0,0,0,1])
        Y = Y + vect2

    print len(X)
    print len(Y)

    x_train, x_test, y_train, y_test = train_test_split(np.asarray(X), np.asarray(Y), test_size=0.33, random_state=None)
    return x_train,x_test,y_train,y_test
'''
x_train = np.asarray(X[:12000], np.float32)
x_test = np.asarray(X[12000:], np.float32)

y_train = np.asarray(Y[:12000], np.float32)
y_test = np.asarray(Y[12000:],np.float32)
print x_train.shape
print x_test.shape

print y_train.shape
print y_test.shape
'''
def nn_model():

    x_train,x_test,y_train,y_test = splitdata(path)    
    model = Sequential()
    model.add(Dense(1000, activation='relu', input_dim=50))
    model.add(Dense(1000, activation='relu'))
    model.add(Dense(1000, activation='relu'))
    model.add(Dense(units = 5, activation='softmax'))

    '''
    hidden1 = Dense(100, activation='relu')(visible)
    hidden2 = Dense(100, activation='relu')(hidden1)
    hidden3 = Dense(100, activation='relu')(hidden2)
    output = Dense(5, activation='softmax')(hidden3)
    model = Model(inputs=visible, outputs=output)
    '''
    # summarize layers
    print(model.summary())



    sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
    model.compile(loss='categorical_crossentropy', optimizer="adam", metrics=['accuracy',mcor,precision,recall, f1])

    model.fit(x_train,y_train, batch_size=32, epochs=50)
    score = model.evaluate(x_test, y_test, batch_size=32)
    prediction = model.predict_classes(x_test)
    print list(prediction.shape)

    f2 = open("prediction.txt","w+")
    f2.write(prediction)

    print score
nn_model()
