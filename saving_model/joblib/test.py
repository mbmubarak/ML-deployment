import joblib
#load the model
model =joblib.load('diabetes_79.pkl')

#in case if you want to scaled data
"""
scalar=joblib.load('scale.pkl')
data = scale.transform([[1,1,1,1,1,1,1,1]])
and finally pass data inside the predict function
"""
result = model.predict([[1,1,1,1,1,1,1,1]]) # predict function expects a 2D array; first two dimensional array thats why [[]]; random 1 is passed, it is passed 8 times becuase as 8 independent columns


#print(result[0]) --> 0.0

if result[0]==1:
    print("diabetic")
else:
    print('not diabetic')