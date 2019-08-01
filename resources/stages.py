from flask_restful import Resource
from models.stage import Stage
from schemas.stage import StageSchema


class StageList(Resource):
    stage_schema = StageSchema()

    def get(self):
        stages = Stage.query.all()

        return {"data": self.stage_schema.dump(stages, many=True)}