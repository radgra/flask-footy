from flask_restful import Resource
from models.player import Player
from schemas.player import PlayerSchema


class PlayerList(Resource):
    player_schema = PlayerSchema()

    def get(self):
        players = Player.query.all()

        return {"data": self.player_schema.dump(players, many=True)}
