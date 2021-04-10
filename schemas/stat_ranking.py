from ma import ma
from marshmallow import fields
from models.stat_ranking import StatRanking
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

class StatRankingSchema(SQLAlchemyAutoSchema):
    
    class Meta:
        model = StatRanking
        include_fk = True