from application import db

class Questions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(50))
    options = db.relationship('Options', backref='questions')

class Options(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    optletter = db.Column(db.String(1))
    option = db.Column(db.String(30))
    status = db.Column(db.String(10))
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'))
