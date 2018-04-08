from utils import *
from flask import Flask, render_template, request, url_for, redirect
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def homepage():
    error = None
    if request.method == 'POST':
        if ValidateUser(request.form['UserName'], request.form['Password']):
            return redirect(url_for('rate', UserName=request.form['UserName']))
        else:
            error = 'Invalid Credentials. Please try again.'
    return render_template('index.html', error=error)

@app.route('/rate')
def rate():
    UserName = request.args['UserName']
    return render_template('rate.html',UserName=UserName, Courses=GetCoursesByUsername(UserName))
