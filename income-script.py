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
fnlwgt = input("Please enter fnlwgt: ")
education = input("Please enter education: ")
education_num = input("Please enter education_num: ")
marital_status = input("Please enter marital_status: ")
occupation = input("Please enter occupation: ")
relationship = input("Please enter relationship: ")
race = input("Please enter race: ")
sex = input("Please enter sex: ")
capital_gain = input("Please enter capital_gain: ")
capital_loss = input("Please enter capital_loss: ")
hours_per_week = input("Please enter hours_per_week: ")
native_country = input("Please enter native_country: ")

data_list = [age, workclass, fnlwgt, education, education_num, marital_status, occupation, relationship, race, sex, capital_gain, capital_loss, hours_per_week, native_country]


data = pd.DataFrame([data_list])


data.columns = ['age', 'workclass', 'fnlwgt', 'education', 'education-num',
       'marital-status', 'occupation', 'relationship', 'race', 'sex',
       'capital-gain', 'capital-loss', 'hours-per-week', 'native-country']

data[['workclass', 'education', 'marital-status', 'occupation', 'relationship', 'race', 'sex', 'native-country']] = data[['workclass', 'education', 'marital-status', 'occupation', 'relationship', 'race', 'sex', 'native-country']].apply(lambda x: label_dict[x.name].transform(x))

data = data.astype(int)

data_xgb = xgb.DMatrix(data)

pred = loaded_model.predict(data_xgb)

income = label_dict['income'].inverse_transform([int(pred[0])])

print("Predicted income is " + str(income[0]))