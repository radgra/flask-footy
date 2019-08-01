from db import db
from sqlalchemy.orm import backref

class Match(db.Model):
    __tablename__ = 'matches'

    id = db.Column(db.Integer, primary_key=True)
    homeTeamId = db.Column(db.Integer, db.ForeignKey("teams.id", ondelete="CASCADE"))
    awayTeamId = db.Column(db.Integer, db.ForeignKey("teams.id", ondelete="CASCADE"))
    tournamentId = db.Column(db.Integer, db.ForeignKey("tournaments.id", ondelete="CASCADE"))
    stageId = db.Column(db.Integer, db.ForeignKey("stages.id", ondelete="CASCADE"))
    
    date = db.Column(db.Date)
    goalsHomeTeam = db.Column(db.Integer)
    goalsAwayTeam = db.Column(db.Integer)

    homeTeam = db.relationship("Team", backref=backref('homeMatches', passive_deletes=False, cascade="all, delete-orphan"), foreign_keys=homeTeamId)
    awayTeam = db.relationship("Team", backref=backref('awayMatches', passive_deletes=False, cascade="all, delete-orphan"), foreign_keys=awayTeamId)
    tournament = db.relationship("Tournament", backref=backref('matches', passive_deletes=False, cascade="all, delete-orphan"))
    stage = db.relationship("Stage", backref=backref('matches', passive_deletes=False, cascade="all, delete-orphan"))

    def __repr__(self):
        return f'{self.date}'