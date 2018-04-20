from utils import *
from flask import Flask, render_template, request, url_for, redirect, session
app = Flask(__name__)
app.secret_key = 'RichardLikesSpaghettiAndMeatBalls'

@app.route('/', methods=['GET', 'POST'])
def homepage():
    message = None
    if 'Message' in request.args:
        message = request.args['Message']
    if request.method == 'POST':
        if ValidateUser(request.form['UserName'], request.form['Password']):
            session['UserName'] = request.form['UserName']
            return redirect(url_for('homescreen'))
        else:
            message = 'Invalid Credentials. Please try again.'
    return render_template('index.html', message=message)

@app.route('/home')
def homescreen():
    return render_template('home.html')

@app.route('/rate', methods=['GET','POST'])
def rate():
    message = None
    UserName = session['UserName']
    if request.method == 'POST':
        CourseInfo = request.form['Course'].split(' - ')
        rating = request.form['rating']
        notes = request.form['Notes']
        success = AddRating(UserName, CourseInfo[0], GetSemesterID(CourseInfo[2]), CourseInfo[1], rating, notes)
        if success:
            message = 'Rating successfully added'
        else:
            message = 'Please do not leave more than one rating per course!'
    return render_template('rate.html',UserName=UserName, Courses=GetCoursesByUsername(UserName), message=message)

@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    if request.method == 'POST':
        if request.form['Password'] != request.form['Verify']:
            error = 'Please make sure your password is typed correctly'
        elif RegisterStudent(request.form['UserName'], request.form['Password'], request.form['FullName']):
            return redirect(url_for('homepage', Message='Account registered successfully!'))
        else:
            error = 'Username already exists in the database'
    return render_template('register.html', error=error)

@app.route('/enroll', methods=['GET','POST'])
def enroll():
    message = None
    UserName = session['UserName']
    if request.method == 'POST':
        CourseCode = request.form['CourseCode']
        success = EnrollStudent(UserName, CourseCode)
        if success:
            message = 'Successfully enrolled into course!'
        else:
            message = "Please make sure that you are providing a valid course code or not enrolling in the same course more than once"
    return render_template('enroll.html',UserName=UserName, message=message)

