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

from application import routes
from application import models
