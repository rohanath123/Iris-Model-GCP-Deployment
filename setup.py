#SETUP SCRIPT FOR CREATING PACKAGE FOR IRIS GCP PRACTICE

from setuptools import setup 

setup(
	name='irisgcppractice_package', 
	version='0.1.5', 
	include_package_data=True, 
	scripts=['preprocess.py', 'custompredict.py']
	)