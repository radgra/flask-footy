from flask_restful import Resource
from models.match import Match
from schemas.match import MatchSchema


class MatchList(Resource):
    match_schema = MatchSchema()

    def get(self):
        matches = Match.query.all()

        return {"data": self.match_schema.dump(matches, many=True)}