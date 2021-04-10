from ma import ma
from marshmallow import fields
from models.squad import Squad
from schemas.player import PlayerSchema
from schemas.tournament import TournamentSchema
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema


class SquadSchema(SQLAlchemyAutoSchema):
    player = fields.Nested(PlayerSchema)
    tournament = fields.Nested(TournamentSchema)
    
    class Meta:
        model = Squad
        include_fk = True
