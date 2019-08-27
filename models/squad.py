from db import db
from sqlalchemy.orm import backref

POSITIONS = ("Bramkarz","Obronca","Pomocnik","Napastnik")


class Squad(db.Model):
    __tablename__ = 'squads'

    id = db.Column(db.Integer, primary_key=True)
    playerId = db.Column(db.Integer, db.ForeignKey("players.id", ondelete="CASCADE"))
    tournamentId = db.Column(db.Integer, db.ForeignKey("tournaments.id", ondelete="CASCADE"))
    appearances = db.Column(db.Integer)
    position = db.Column(db.String)
    goals = db.Column(db.Integer)

    player = db.relationship("Player", backref=backref('squads', passive_deletes=False, cascade="all, delete-orphan"))
    tournament = db.relationship("Tournament", backref=backref('squads', passive_deletes=False, cascade="all, delete-orphan"))

    # def __repr__(self):

