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

@app.route('/rate', methods=['GET','POST'])
def rate():
    message = None
    UserName = request.args['UserName']
    if request.method == 'POST':
        CourseInfo = request.form['Course'].split(' - ')
        rating = request.form['rating']
        notes = request.form['Notes']
        print(UserName, CourseInfo[0], str(GetSemesterID(CourseInfo[2])), CourseInfo[1], rating, notes)
        success = AddRating(UserName, CourseInfo[0], GetSemesterID(CourseInfo[2]), CourseInfo[1], rating, notes)
        print(success)
        if success:
            message = 'Rating successfully added'
        else:
            message = 'Please do not leave more than one rating per class'
    return render_template('rate.html',UserName=UserName, Courses=GetCoursesByUsername(UserName), message=message)
