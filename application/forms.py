from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

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

class AnswerQuestion(FlaskForm):
    sel_opt = SelectField('Select your answer:', choices=[('A','A'),('B','B'),('C','C'),('D','D')])
    submit = SubmitField('Submit Answer')
