from db import db
from sqlalchemy.orm import backref


RANKING_TYPES = (
    "goals",
    "matches"
)

class StatRanking(db.Model):
    __tablename__ = 'stat_ranking'

    id = db.Column(db.Integer, primary_key=True)
    statId = db.Column(db.Integer, db.ForeignKey("stats.id", ondelete="CASCADE"))
    rankingType = db.Column(db.String)
    position = db.Column(db.Integer)
    
    stat = db.relationship("Stat", backref=backref('statRankings', passive_deletes=False, cascade="all, delete-orphan"))


    def __repr__(self):
        return self.position