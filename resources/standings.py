from flask_restful import Resource
from models.standing import Standing
from schemas.standing import StandingSchema
from flask import request



class StandingList(Resource):
    standing_schema = StandingSchema()

    def get(self):
        query = Standing.query
        wc_year = request.args.get('year')
        
        if wc_year:
            query = Standing.query.filter(Standing.tournament.has(year=wc_year))
        
        standings = query.all()

        return {"data": self.standing_schema.dump(standings, many=True)}