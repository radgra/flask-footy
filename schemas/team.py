from ma import ma
from models.team import Team


class TeamSchema(ma.ModelSchema):

    class Meta:
        model = Team
        include_fk = True
