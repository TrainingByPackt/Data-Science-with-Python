import xgboost as xgb
from sklearn.preprocessing import LabelEncoder
import pickle
import pandas as pd

def load_obj(file):
	with open(file + '.pkl', 'rb') as f:
		return pickle.load(f)
		
loaded_model = xgb.Booster({'nthread': 8})
loaded_model.load_model('income-model.model')

label_dict = load_obj('income_labels')


age = input("Please enter age: ")
workclass = input("Please enter workclass: ")
education_num = input("Please enter education_num: ")
occupation = input("Please enter occupation: ")
capital_gain = input("Please enter capital_gain: ")
capital_loss = input("Please enter capital_loss: ")
hours_per_week = input("Please enter hours_per_week: ")

data_list = [age, workclass, education_num, occupation, capital_gain, capital_loss, hours_per_week]


data = pd.DataFrame([data_list])


data.columns = ['age', 'workclass', 'education-num',
       'occupation', 'capital-gain', 'capital-loss', 'hours-per-week']

data[['workclass', 'occupation']] = data[['workclass', 'occupation']].apply(lambda x: label_dict[x.name].transform(x))

data = data.astype(int)

data_xgb = xgb.DMatrix(data)

pred = loaded_model.predict(data_xgb)

income = label_dict['income'].inverse_transform([int(pred[0])])

print("Predicted income is " + str(income[0]))