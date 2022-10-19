import pandas as pd
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
import pickle # to save the load the model

url="https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"

names = ['preg','plas','pres','skin','test', 'mass','predi','age','class']
dataframe = pd.read_csv(url, names=names)
print(dataframe)

#seperate the independent and target variable
array = dataframe.values
X = array[:,0:8]
y=array[:,8]

# train test split
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.2, random_state=101)

# fir the model
model = LogisticRegression()
model.fit(X_train,y_train)

# accuracy
result = model.score(X_test, y_test)
print(result)

#saving the model
filename = "diabetes_79.pkl" #naming convention daibetes - dataset and 79 - accuracy got
# this diabetes_79.pkl is encrypted and this is called serialization (serialized data)
pickle.dump(model, open(filename, 'wb')) # wb - becas it is byte file and we need to write so opening write mode


#only chnages compared to job lib are:
#1.import pickle instaed of joblib at the top
#2.pickle.dump instaed of joblib.dump and second parameter is Open(filename,'wb') need to be passed