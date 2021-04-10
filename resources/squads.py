from flask_restful import Resource
from models.squad import Squad
from schemas.squad import SquadSchema
from flask import request


class SquadList(Resource):
    squad_schema = SquadSchema()

    def get(self):
        query = Squad.query
        wc_year = request.args.get('year')
        
        if wc_year:
            query = Squad.query.filter(Squad.tournament.has(year=wc_year))

        squads = query.all()
        return {"data": self.squad_schema.dump(squads, many=True)}
