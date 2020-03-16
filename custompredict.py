#CUSTOM PREDICTOR CLASS FOR CUSTOM PREDICTION FOR IRIS GCP PRACTICE

import pickle 
import numpy as np 
import os

class CustomPredictor(object):
	def __init__(self, model):
		self._model = model

	def predict(self, instances, **kwargs):

		inputs = np.asarray(instances)
		outputs = self._model.predict(inputs)

		return outputs.tolist()

		
	@classmethod 
	def from_path(cls, model_dir):

		model_path = os.path.join(model_dir, 'model.pkl')
		with open(model_path, 'rb') as f:
			model = pickle.load(f)

		return cls(model)