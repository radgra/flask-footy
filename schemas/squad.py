from ma import ma
from marshmallow import fields
from models.squad import Squad
from schemas.player import PlayerSchema
from schemas.tournament import TournamentSchema

class SquadSchema(ma.ModelSchema):
    player = fields.Nested(PlayerSchema,exclude=('squads',))
    tournament = fields.Nested(TournamentSchema,exclude=('squads',))
    
    class Meta:
        model = Squad
        include_fk = True
