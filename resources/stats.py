from flask_restful import Resource
from models.stat import Stat
from schemas.stat import StatSchema


class StatList(Resource):
    stat_schema = StatSchema()

    def get(self):
        stats = Stat.query.all()

        return {"data": self.stat_schema.dump(stats, many=True)}