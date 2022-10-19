# pip install flask
from flask import Flask, render_template, request
import joblib #you need to use same model you want to deploy ex. pickle or joblib
# initialise the app
app = Flask(__name__)

#loads the model
model=joblib.load('diabetes_79.pkl')

@app.route('/')
def home():
    return render_template('main.html')

@app.route('/contact-us')      
def contact():
    return render_template('contact.html')

@app.route('/blog')
def blog():
    return "blog"

@app.route('/form', methods=['post'])
def form():
    #first_name = request.form.get('first')
    #second_name = request.form.get('second')
    #phone = request.form.get('phone')
    #mail = request.form.get('email')
    #exp = request.form.get('exp')

    #print(first_name, second_name, phone,exp, mail)

    preg = request.form.get('preg')
    plas = request.form.get('plas')
    pres = request.form.get('pres')
    skin = request.form.get('skin')
    test = request.form.get('test')
    mass = request.form.get('mass')
    pedi = request.form.get('pedi')
    age = request.form.get('age')

    result = model.predict([[preg, plas, pres, skin, test, mass, pedi, age]])
    
    if result[0]==1:
        data = 'person is diabetic'
    else:
        data = 'person is not diabetic'

    return data
    


# run the app
app.run(debug=True) # debug = True means we are in development phase; everytime a change is made tge server is automatically reloaded instead of maunally reloading
