from db import db
from sqlalchemy.orm import backref


class Stat(db.Model):
    __tablename__ = 'stats'

    id = db.Column(db.Integer, primary_key=True)
    playerId = db.Column(db.Integer, db.ForeignKey("players.id", ondelete="CASCADE"))
    goals = db.Column(db.Integer)
    matches = db.Column(db.Integer)
    
    player = db.relationship("Player", backref=backref('stats', passive_deletes=False, cascade="all, delete-orphan"))


    def __repr__(self):
        return self.name