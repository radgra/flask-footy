from ma import ma
from models.match import Match
from schemas.team import TeamSchema
# from marshmallow import fields
from schemas.tournament import TournamentSchema
from schemas.goal import GoalSchema
from schemas.stage import StageSchema
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, fields


class MatchSchema(SQLAlchemyAutoSchema):
    homeTeam = fields.Nested(TeamSchema)
    awayTeam = fields.Nested(TeamSchema)
    tournament = fields.Nested(TournamentSchema)
    stage = fields.Nested(StageSchema)
    goals = fields.Nested(GoalSchema,many=True)

    class Meta:
        model = Match
        include_fk = True
