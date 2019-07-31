from flask_restful import Resource
from models.round import Round
from schemas.round import RoundSchema


class RoundList(Resource):
    round_schema = RoundSchema()

    def get(self):
        rounds = Round.query.all()

        return {"data": self.round_schema.dump(rounds, many=True)}