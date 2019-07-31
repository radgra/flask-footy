from db import db


class Tournament(db.Model):
    __tablename__ = 'tournaments'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    image = db.Column(db.String(200))
    year = db.Column(db.Integer)

    def __repr__(self):
        return self.title
