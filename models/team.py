from db import db


class Team(db.Model):
    __tablename__ = 'teams'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    flag = db.Column(db.String(200))

    def __repr__(self):
        return self.name
