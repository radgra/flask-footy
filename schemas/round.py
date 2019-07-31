from ma import ma
from models.round import Round


class RoundSchema(ma.ModelSchema):

    class Meta:
        model = Round
        include_fk = True
