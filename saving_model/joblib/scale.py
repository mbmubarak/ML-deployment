# to apply feature scaling transform to test_data
scale = Standard_scalar()
scaling = scale.fit(x_train)


filename = "scale_train.pkl" #naming convention daibetes - dataset and 79 - accuracy got; extn.pkl
# this diabetes_79.pkl is encrypted and this kind of files are called serialized data (serialization) so that loading does faster
joblib.dump(model, filename)