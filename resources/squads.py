from flask_restful import Resource
from models.squad import Squad
from schemas.squad import SquadSchema


class SquadList(Resource):
    squad_schema = SquadSchema()

    def get(self):
        squads = Squad.query.all()

        return {"data": self.squad_schema.dump(squads, many=True)}
