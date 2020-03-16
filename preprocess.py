#IRIS GCP PRACTICE, PREPROCESS DATA FILE

import pandas as pd 
import numpy as np 


def num_cat_labels(y):
	labels = list(y[0].unique())
	label_dict = {labels[i]:i for i in range(len(labels))}
	
	for i in range(len(y)):
		y[0].iloc[i] = label_dict[y[0].iloc[i]]
	y = y.astype('int')

	return y

def make_x_y(df):
	Y = pd.DataFrame(df.Species.values)
	X = df.drop(['Species', 'Id'], axis = 1)
	return X, Y

def clean(df):
	X, Y = make_x_y(df)
	Y = num_cat_labels(Y)

	return X, Y


