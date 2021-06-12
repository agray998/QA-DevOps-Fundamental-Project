from application import db

class Questions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(50))
    options = db.relationship('Options', backref='question')
    def __repr__(self):
        return f"Question {self.id}) {self.question}"

class Options(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    optletter = db.Column(db.String(1))
    option = db.Column(db.String(30))
    status = db.Column(db.String(10))
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'))
    def __repr__(self):
        return f"{self.optletter}) {self.option}"

class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    status = db.Column(db.String(10))
    def __repr__(self):
        return f"{self.name} - {self.status}"

class Result(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    score = db.Column(db.Integer)
    date = db.Column(db.DateTime)
