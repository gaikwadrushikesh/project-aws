import re
from flask import Flask, jsonify, render_template, request,redirect, url_for
import config
from utils import MedicalInsurence

app = Flask(__name__)

##########################################################################
########################## Login API ######################################
##########################################################################

@app.route('/') 
def hello_flask():
    return 'Hello'

@app.route('/result')
def result():
    return "Hello Rushikesh"

@app.route('/login')
def login():
    print("HELLO")
    if request.method == 'POST':
        data = request.form
        name = data['name']
        print("Name ::::",name)
        return redirect(url_for('result',name = name))

    if request.method == 'GET':
        name = request.args.get('name')
        print("Name ::::",name)
        return redirect(url_for('result',name = name))

#########################################################################

@app.route('/predict_charges')
def get_insurance_charges():
        data = request.get(json)
        age = eval(data['age'])
        sex = data['sex']
        bmi = eval(data['bmi'])
        children = eval(data['children'])
        smoker = data['smoker']
        region = data['region']

        print("age, sex, bmi,children,smoker, region",age, sex, bmi,children,smoker, region)
        med_ins = MedicalInsurence(age, sex, bmi,children,smoker, region)
        charges = med_ins.get_predicted_charges()

        return charges
 

@app.route('/testing/<student_name>')
def testing1(student_name):
    return f"Hello {student_name}"

@app.route('/marks/<float:score>')
def marks(score):
    print(type (score))
    return f"Score is : {score}"


if __name__ == "__main__":
    app.run(port = config.PORT_NUMBER)
