from flask_restful import Resource
from models.stat_ranking import StatRanking
from schemas.stat_ranking import StatRankingSchema


class StatRankingList(Resource):
    sr_schema = StatRankingSchema()

    def get(self):
        stat_rankings = StatRanking.query.all()

        return {"data": self.sr_schema.dump(stat_rankings, many=True)}