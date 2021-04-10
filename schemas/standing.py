from ma import ma
from models.standing import Standing
# from marshmallow import fields
from schemas.team import TeamSchema
from schemas.stage import StageSchema
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema,fields

class StandingSchema(SQLAlchemyAutoSchema):
    team = fields.Nested(TeamSchema)
    stage = fields.Nested(StageSchema)

    class Meta:
        model = Standing
        include_fk = True
