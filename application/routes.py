from application import app, db, AddQuestion, UpdateQuestion, AddOptions
from application.models import Questions, Options
from flask import render_template, request, redirect, url_for

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/questions')
def questions():
    questions = Questions.query.all()
    return render_template('questions.html', questions=questions)

@app.route('/add-question', methods=['GET','POST'])
def add_q():
    form = AddQuestion()
    if request.method == 'POST':
        q_name = form.q_name.data
        newquest = Questions(question = q_name)
        db.session.add(newquest)
        db.session.commit()
        return redirect(url_for('questions'))
    return render_template('add_question.html', form=form)

@app.route('/add-options/<int:qid>', methods=['GET','POST'])
def add_o(qid):
    form = AddOptions()
    if request.method == 'POST':
        o_letter = form.o_letter.data
        option = form.o_option.data
        o_status = form.o_status.data
        quest_id = qid
        newopt = Options(optletter = o_letter, option = option, status = o_status, question_id = qid)
        db.session.add(newopt)
        db.session.commit()
        question = Questions.query.filter_by(id = qid).first()
        question.options = Options.query.filter_by(question_id = qid).all()
        db.session.commit()
        return redirect(url_for('questions'))
    return render_template('add_options.html', form=form)
