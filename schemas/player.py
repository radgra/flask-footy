from ma import ma
from models.player import Player


class PlayerSchema(ma.ModelSchema):

    class Meta:
        model = Player
        include_fk = True
