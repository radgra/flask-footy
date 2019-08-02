from ma import ma
from models.match import Match
from schemas.team import TeamSchema
from marshmallow import fields
from schemas.tournament import TournamentSchema
from schemas.goal import GoalSchema
from schemas.stage import StageSchema


class MatchSchema(ma.ModelSchema):
    homeTeam = fields.Nested(TeamSchema, exclude=('awayMatches',"homeMatches",'standings'))
    awayTeam = fields.Nested(TeamSchema, exclude=('awayMatches',"homeMatches",'standings'))
    tournament = fields.Nested(TournamentSchema, exclude=('matches',"squads","standings"))
    stage = fields.Nested(StageSchema, exclude=('standings','matches'))
    goals = fields.Nested(GoalSchema,exclude=('player.stats',),many=True)

    class Meta:
        model = Match
        include_fk = True
