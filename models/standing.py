from db import db
from sqlalchemy.orm import backref

class Standing(db.Model):
    __tablename__ = 'standings'

    id = db.Column(db.Integer, primary_key=True)
    tournamentId = db.Column(db.Integer, db.ForeignKey("tournaments.id", ondelete="CASCADE"))
    teamId = db.Column(db.Integer, db.ForeignKey("teams.id", ondelete="CASCADE"))
    stageId = db.Column(db.Integer, db.ForeignKey("stages.id", ondelete="CASCADE"))

    position = db.Column(db.Integer)
    goalsScored = db.Column(db.Integer)
    goalsConceded = db.Column(db.Integer)
    points = db.Column(db.Integer)
    wins = db.Column(db.Integer)
    losses = db.Column(db.Integer)
    draws = db.Column(db.Integer)


    tournament = db.relationship("Tournament", backref=backref('standings', passive_deletes=False, cascade="all, delete-orphan"))
    team = db.relationship("Team", backref=backref('standings', passive_deletes=False, cascade="all, delete-orphan"))
    stage = db.relationship("Stage", backref=backref('standings', passive_deletes=False, cascade="all, delete-orphan"))

    def __repr__(self):
        return f'{self.date}'