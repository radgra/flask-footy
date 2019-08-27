from db import db


class Stage(db.Model):
    __tablename__ = 'stages'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    position = db.Column(db.Integer)
    tournamentId = db.Column(db.Integer, db.ForeignKey("tournaments.id", ondelete="CASCADE"))

    tournament = db.relationship("Tournament", backref=backref('stages', passive_deletes=False, cascade="all, delete-orphan"))

    def __repr__(self):
        return self.name
