import sklearn 
import pickle
import custompredict

#model = pickle.load(open('C:/Users/Rohan/Desktop/Personal/Work/GURGAON STUFF/IrisPractice/models/model.pkl', 'rb'))
obj = custompredict.CustomPredictor(0)
model = obj.from_path('C:/Users/Rohan/Desktop/Personal/Work/GURGAON STUFF/IrisPractice/models')

print(model.predict([[5.7, 2.9, 4.2, 1.3]]))

