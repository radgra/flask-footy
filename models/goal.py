from db import db
from sqlalchemy.orm import backref

class Goal(db.Model):
    __tablename__ = 'goals'

    id = db.Column(db.Integer, primary_key=True)
    matchId = db.Column(db.Integer, db.ForeignKey("matches.id", ondelete="CASCADE"))
    playerId = db.Column(db.Integer, db.ForeignKey("players.id", ondelete="CASCADE"))
    minute = db.Column(db.Integer)
    awayTeamGoal = db.Column(db.Boolean, default=False)
    homeTeamGoal = db.Column(db.Boolean, default=False)

    match = db.relationship("Match", backref=backref('goals', passive_deletes=False, cascade="all, delete-orphan"))
    player = db.relationship("Player", backref=backref('goals', passive_deletes=False, cascade="all, delete-orphan"))

    def __repr__(self):
        return f'{self.minute}'