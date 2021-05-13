from application import app, db, AddQuestion, UpdateQuestion, AddOptions, UpdateOptions, AnswerQuestion
from application.models import Questions, Options, Answer
from flask import render_template, request, redirect, url_for

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/questions')
def questions():
    questions = Questions.query.all()
    return render_template('questions.html', questions=questions)

@app.route('/question-<int:qid>')
def question(qid):
    question = Questions.query.filter_by(id=qid).first()
    maxid = Questions.query.order_by(Questions.id.desc()).first().id
    return render_template('question.html', question=question, maxid=maxid)

@app.route('/add-question', methods=['GET','POST'])
def add_q():
    form = AddQuestion()
    if request.method == 'POST':
        q_name = form.q_name.data
        newquest = Questions(question = q_name)
        db.session.add(newquest)
        db.session.commit()
        return redirect(url_for('add_o', qid=newquest.id))
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
        return redirect(url_for('add_o', qid=qid))
    return render_template('add_options.html', form=form)

@app.route('/update-question/<int:qid>', methods=['GET','POST'])
def update_q(qid):
    form = UpdateQuestion()
    if request.method == 'POST':
        q_name = form.q_name.data
        question = Questions.query.filter_by(id=qid).first()
        question.question = q_name
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('update_question.html', form=form)

@app.route('/update-options/<int:oid>', methods=['GET','POST'])
def update_o(oid):
    form = UpdateOptions()
    if request.method == 'POST':
        o_letter = form.o_letter.data
        option = form.o_option.data
        o_status = form.o_status.data
        opt_id = oid
        opt = Options.query.filter_by(id=oid).first()
        qid = Questions.query.filter_by(id=opt.question_id).first()
        opt.optletter = o_letter
        opt.option = option
        opt.status = o_status
        db.session.commit()
        return redirect(url_for('question', qid=qid))
    return render_template('update_options.html', form=form)

@app.route('/delete-option/<int:oid>')
def delete_o(oid):
    option = Options.query.filter_by(id=oid).first()
    qid = Questions.query.filter_by(id=option.question_id).first()
    db.session.delete(option)
    db.session.commit()
    return redirect(url_for('question', qid=qid))

@app.route('/delete-question/<int:qid>')
def delete_q(qid):
    question = Questions.query.filter_by(id=qid).first()
    options = Options.query.filter_by(question_id=qid).all()
    db.session.delete(question)
    for option in options:
        db.session.delete(option)
    db.session.commit()
    return redirect(url_for('questions'))

@app.route('/answer-<int:qid>', methods=['GET','POST'])
def answer_q(qid):
    form = AnswerQuestion()
    question = Questions.query.filter_by(id=qid).first()
    options = Options.query.filter_by(question_id=qid).all()
    if request.method == 'POST':
        ans_opt = form.sel_opt.data
        ans_status = Options.query.filter_by(question_id = qid, optletter = ans_opt).first().status
        newans = Answer(name = ans_opt, status = ans_status)
        db.session.add(newans)
        db.session.commit()
        if qid == Questions.query.order_by(Questions.id.desc()).first().id:
            return redirect(url_for('questions'))
        else:
            return redirect(url_for('answer_q', qid=qid+1))
    return render_template('answer-question.html', form=form, question=question, options=options)
