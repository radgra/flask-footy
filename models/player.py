from db import db


class Player(db.Model):
    __tablename__ = 'players'

    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(100))
    lastName = db.Column(db.String(100))
    born = db.Column(db.Date)

    def get_fullname(self):
        return f'{self.firstName} {self.lastName}'

    def __repr__(self):
        return self.get_fullname()
