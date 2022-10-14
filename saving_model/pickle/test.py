import joblib
#load the model
model =pickle.load(open('diabetes_79.pkl')
result = model.predict([[1,1,1,1,1,1,1,1]]) # random 1 is passed, it is passed 8 times becuase as 8 independent columns

if result[0]==1:
    print("diabetic")
else:
    print('not diabetic')