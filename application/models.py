from application import db

class Questions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(50))
    options = db.relationship('Options', backref='question')

class Options(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    optletter = db.Column(db.Char())
    option = db.Column(db.String(30))
    status = db.Column(db.String(10))
    question = db.Column(db.Integer, db.ForeignKey('question.id'))
