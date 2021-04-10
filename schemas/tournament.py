from ma import ma
from models.tournament import Tournament
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema


class TournamentSchema(SQLAlchemyAutoSchema):

    class Meta:
        model = Tournament
        include_fk = True
