# Iris-Model-GCP-Deployment
Created a simple Iris SkLearn Logisitic Regression Model, but code is uniform with GCP trained model deployment best practices.

GCP Deployment best practices essentially include creating clean, understandable code, that can be easily managed and handled by Google Cloud when it comes to Custom Prediction Pipelines. 

While Scikit-Learn is a supported package on Google's AI-Platform prediction instances (2.1 and 1.15, and even before), I wanted to try a Custom Prediction Pipeline because I code mostly with Pytorch and not Tensorflow, and will mostly be deploying Pytorch models on the cloud. 

createModel.py, preprocess.py are both files used to create the trained Logistic Regression model and preprocess the data in that order. 

The really interesting file is custompredict.py, which is the file that AI-Platform will run in order to get custom online predictions from the deployed model on the cloud. It includes a .predict() method that is invoked when predictions are to be made, before which a classmethod .from_path() method is invoked to load the saved .pkl model (and any preprocessing .pkl models, not included here).

setup.py is a script that uses the setuptools package to create a tar-ball package of all the scripts that AIP requires to get custom online predictions. dist is the folder that contains this tar-ball package. 

instances.json, inst2.json are JSON files that contain testing data in the exact format that is required by AIP to input into the model for predictions. AIP expects the data to be in a JSON format, which is then de-serialized automaticaly in the cloud, run through the model, re-serialized and sent back. 
