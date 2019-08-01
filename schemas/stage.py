from ma import ma
from models.stage import Stage


class StageSchema(ma.ModelSchema):

    class Meta:
        model = Stage
        include_fk = True
