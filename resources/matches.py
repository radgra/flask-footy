from flask_restful import Resource
from models.match import Match
from schemas.match import MatchSchema
from flask import request

class MatchList(Resource):
    match_schema = MatchSchema()

    def get(self):
        query = Match.query
        wc_year = request.args.get('year')
        
        if wc_year:
            query = Match.query.filter(Match.tournament.has(year=wc_year))
        
        matches = query.all()

        return {"data": self.match_schema.dump(matches, many=True)}