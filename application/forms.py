from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

class AddQuiz(FlaskForm):
    quiz_name = StringField('Quiz Title', validators=[DataRequired(message="This field cannot be left blank")])
    submit = SubmitField('Add Quiz')

class AddQuestion(FlaskForm):
    q_name = StringField('Question', validators=[DataRequired(message="This field cannot be left blank")])
    quiz = SelectField('Add to quiz:', choices=[])
    submit = SubmitField('Add Question')

class UpdateQuestion(FlaskForm):
    q_name = StringField('Question', validators=[DataRequired(message="This field cannot be left blank")])
    submit = SubmitField('Update Question')

class AddOptions(FlaskForm):
    o_letter = SelectField('Letter', choices=[('A','A'),('B','B'),('C','C'),('D','D')])
    o_option = StringField('Option', validators=[DataRequired(message="This field cannot be left blank")])
    o_status = SelectField('Correct/incorrect', choices=[('correct','Correct'),('incorrect','Incorrect')])
    submit = SubmitField('Add Option')

class UpdateOptions(FlaskForm):
    o_letter = SelectField('Letter', choices=[('A','A'),('B','B'),('C','C'),('D','D')])
    o_option = StringField('Option', validators=[DataRequired(message="This field cannot be left blank")])
    o_status = SelectField('Correct/incorrect', choices=[('correct','Correct'),('incorrect','Incorrect')])
    submit = SubmitField('Update Option')

class AnswerQuestion(FlaskForm):
    sel_opt = SelectField('Select your answer:', choices=[])
    submit = SubmitField('Submit Answer')
