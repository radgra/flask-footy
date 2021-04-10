from ma import ma
from models.goal import Goal
from schemas.player import PlayerSchema
from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

class GoalSchema(ma.SQLAlchemyAutoSchema):
    player = fields.Nested(PlayerSchema)

    class Meta:
        model = Goal
        include_fk = True
