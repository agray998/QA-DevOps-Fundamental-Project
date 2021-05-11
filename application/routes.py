from application import app, db, AddQuestion, UpdateQuestion
from application.models import Questions
from flask import render_template, request, redirect, url_for

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/questions')
def questions():
    questions = Questions.query.all()
    return render_template('questions.html', questions=questions)
