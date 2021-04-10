from ma import ma
from models.team import Team
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema


class TeamSchema(SQLAlchemyAutoSchema):

    class Meta:
        model = Team
        include_fk = True
