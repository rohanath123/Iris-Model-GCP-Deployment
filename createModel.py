#TRAINING AND CREATING MODEL FOR IRIS GCP PRACTICE
import pandas as pd 
import numpy as np 

import sklearn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

import preprocess

import pickle

df = pd.read_csv("D:/Machine Learning Datasets/iris-species/Iris.csv")
X, Y = preprocess.clean(df)

model = LogisticRegression()
model.fit(X, Y)
pickle.dump(model, open('./models/model.pkl', 'wb'))
