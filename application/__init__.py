from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('secretkey')

db = SQLAlchemy(app)

class AddQuestion(FlaskForm):
    q_name = StringField('Question', validators=[DataRequired()])
    submit = SubmitField('Add Question')

class UpdateQuestion(FlaskForm):
    q_name = StringField('Question', validators=[DataRequired()])
    submit = SubmitField('Update Question')

class AddOptions(FlaskForm):
    o_letter = SelectField('Letter', choices=[('A','A'),('B','B'),('C','C'),('D','D')])
    o_option = StringField('Option', validators=[DataRequired()])
    o_status = SelectField('Correct/incorrect', choices=[('correct','Correct'),('incorrect','Incorrect')])
    submit = SubmitField('Add Option')

class UpdateOptions(FlaskForm):
    o_letter = SelectField('Letter', choices=[('A','A'),('B','B'),('C','C'),('D','D')])
    o_option = StringField('Option', validators=[DataRequired()])
    o_status = SelectField('Correct/incorrect', choices=[('correct','Correct'),('incorrect','Incorrect')])
    submit = SubmitField('Update Option')

from application import routes
from application import models
