from ma import ma
from models.standing import Standing
from marshmallow import fields
from schemas.team import TeamSchema
from schemas.stage import StageSchema

class StandingSchema(ma.ModelSchema):
    team = fields.Nested(TeamSchema,exclude=("homeMatches","awayMatches","standings"))
    stage = fields.Nested(StageSchema, exclude=('standings',"matches"))

    class Meta:
        model = Standing
        include_fk = True
