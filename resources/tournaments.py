from flask_restful import Resource
from models.tournament import Tournament
from schemas.tournament import TournamentSchema


class TournamentList(Resource):
    tournament_schema = TournamentSchema()

    def get(self):
        tournaments = Tournament.query.all()

        return {"data": self.tournament_schema.dump(tournaments, many=True)}
