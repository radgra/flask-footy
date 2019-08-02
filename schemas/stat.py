from ma import ma
from marshmallow import fields
from models.stat import Stat
from schemas.player import PlayerSchema
from schemas.stat_ranking import StatRankingSchema

class StatSchema(ma.ModelSchema):
    player = fields.Nested(PlayerSchema,exclude=('squads','stats','goals'))
    statRankings = fields.Nested(StatRankingSchema, exclude=('statId',), many=True)
    
    class Meta:
        model = Stat
        include_fk = True
