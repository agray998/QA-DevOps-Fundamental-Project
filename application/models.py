from application import db

class Questions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(100))
    options = db.relationship('Options', backref='question')

class Options(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    optletter = db.Column(db.Char())
    option = db.Column(db.String(30))
    question = db.Column(db.Integer, db.ForeignKey('question.id'))
