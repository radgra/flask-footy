from ma import ma
from marshmallow import fields
from models.stat_ranking import StatRanking

class StatRankingSchema(ma.ModelSchema):
    
    class Meta:
        model = StatRanking
        include_fk = True