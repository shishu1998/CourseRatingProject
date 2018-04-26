from utils import *
from flask import Flask, render_template, request, url_for, redirect, session
from functools import wraps
import math
app = Flask(__name__)
app.secret_key = 'super secret key'

def checkLoggedIn(func):
	@wraps(func)
	def wrap():
		if 'UserName' in session:
			return func()
		else:
			return 'You are not logged in'
	return wrap

def checkIsProfessor(func):
	@wraps(func)
	def wrap():
		if 'UserName' in session and GetUserType(session['UserName']) == 'Professor':
			return func()
		else:
			return 'You are not allowed here'
	return wrap

@app.route('/', methods=['GET', 'POST'])
def homepage():
	message = None
	if 'Message' in request.args:
		message = request.args['Message']
	if request.method == 'POST':
		if ValidateUser(request.form['UserName'], request.form['Password']):
			UserName = request.form['UserName']
			session['UserName'] = UserName
			if GetUserType(UserName) == 'Student':
				return redirect(url_for('homescreen'))
			else:
				return redirect(url_for('report'))
		else:
			message = 'Invalid Credentials. Please try again.'
	return render_template('index.html', message=message)

@app.route('/home')
@checkLoggedIn
def homescreen():
	return render_template('home.html')
	
@app.route('/logout')
def logout():
	session.pop('UserName', None)
	return redirect(url_for('homepage', Message='Logged out successfully!'))

@app.route('/rate', methods=['GET','POST'])
@checkLoggedIn
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
@checkLoggedIn
def enroll():
	message = None
	UserName = session['UserName']
	if request.method == 'POST':
		CourseCode = request.form['CourseCode']
		success = EnrollStudent(UserName, CourseCode)
		if success:
			message = 'Successfully enrolled into course!'
		else:
			message = "Please make sure that you are providing a valid course code for a course that you're not enrolled in"
	return render_template('enroll.html',UserName=UserName, message=message)

@app.route('/report', methods=['GET','POST'])
@checkIsProfessor
@checkLoggedIn
def report():
	message = None
	showChart = False
	showNotes = False
	labels = ["Very Good", "Good", "Average", "Bad", "Very Bad"]
	values = [0, 0, 0, 0, 0]
	notes = []
	maxValue = 10
	numOfNotes = 0
	UserName = session['UserName']
	if request.method == 'POST':
		CourseInfo = request.form['Course'].split(' - ')
		ratingData = GetRatings(CourseInfo[0], CourseInfo[1], CourseInfo[2]);
		ratingCount = GetRatingsCount(CourseInfo[0], CourseInfo[1], CourseInfo[2]);
		maxRatingCount, numOfNotes = BuildReport(values, notes, ratingData, ratingCount)
		maxValue = int(math.ceil(maxRatingCount / 10.0)) * 10
		if maxValue:
			showChart = True
		if numOfNotes:	
			showNotes = True
		message = str(len(ratingData)) + " rating(s) for the course: " + request.form['Course']
	return render_template('report.html', Courses=GetCoursesByUsername(UserName), message=message, values=values, labels=labels, maxValue=maxValue, notes=notes, showChart=showChart, showNotes=showNotes)
