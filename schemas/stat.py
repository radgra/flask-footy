from ma import ma
# from marshmallow import fields
from models.stat import Stat
from schemas.player import PlayerSchema
from schemas.stat_ranking import StatRankingSchema
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, fields

class StatSchema(SQLAlchemyAutoSchema):
    player = fields.Nested(PlayerSchema)
    statRankings = fields.Nested(StatRankingSchema, exclude=('statId',), many=True)
    
    class Meta:
        model = Stat
        include_fk = True
