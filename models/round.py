from db import db


class Round(db.Model):
    __tablename__ = 'rounds'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    position = db.Column(db.Integer)

    def __repr__(self):
        return self.name
