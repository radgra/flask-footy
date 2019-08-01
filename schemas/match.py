from ma import ma
from models.match import Match
from schemas.team import TeamSchema
from marshmallow import fields
from schemas.tournament import TournamentSchema
from schemas.goal import GoalSchema


class MatchSchema(ma.ModelSchema):
    homeTeam = fields.Nested(TeamSchema, exclude=('awayMatches',"homeMatches",))
    awayTeam = fields.Nested(TeamSchema, exclude=('awayMatches',"homeMatches",))
    tournament = fields.Nested(TournamentSchema, exclude=('matches',"squads",))
    goals = fields.Nested(GoalSchema, exclude=(),many=True)

    class Meta:
        model = Match
        include_fk = True
