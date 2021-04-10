from ma import ma
from models.stage import Stage
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema


class StageSchema(SQLAlchemyAutoSchema):

    class Meta:
        model = Stage
        include_fk = True
