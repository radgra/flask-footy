from ma import ma
from models.goal import Goal
from schemas.player import PlayerSchema
from marshmallow import fields


class GoalSchema(ma.ModelSchema):
    player = fields.Nested(PlayerSchema, exclude=('goals','squads'))

    class Meta:
        model = Goal
        include_fk = True
