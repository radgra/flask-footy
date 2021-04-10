from ma import ma
from models.player import Player
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

class PlayerSchema(SQLAlchemyAutoSchema):

    class Meta:
        model = Player
        include_fk = True
