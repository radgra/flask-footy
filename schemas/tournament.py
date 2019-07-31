from ma import ma
from models.tournament import Tournament


class TournamentSchema(ma.ModelSchema):

    class Meta:
        model = Tournament
        include_fk = True
