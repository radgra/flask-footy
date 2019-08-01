from flask_restful import Resource
from models.standing import Standing
from schemas.standing import StandingSchema


class StandingList(Resource):
    standing_schema = StandingSchema()

    def get(self):
        standings = Standing.query.all()

        return {"data": self.standing_schema.dump(standings, many=True)}