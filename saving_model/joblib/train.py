import pandas as pd
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
import joblib # to save the load the model

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

# fit the model
model = LogisticRegression()
model.fit(X_train,y_train)

# accuracy
result = model.score(X_test, y_test)
print(result)

#saving the model
filename = "diabetes_79.pkl" #naming convention daibetes - dataset and 79 - accuracy got; extn.pkl
# this diabetes_79.pkl is encrypted and this kind of files are called serialized data (serialization) so that loading does faster
joblib.dump(model, filename)

#this will dump the model and saves a file in the current working dir; here in this ex. it creates a file called "diabetes_79.pkl" under joblib


# to apply feature scaling transform to test_data
""" 
scale = Standard_scalar()
scaling = scale.fit(x_train)


filename = "scale_train.pkl" 
joblib.dump(model, filename)


"""