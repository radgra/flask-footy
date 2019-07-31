from flask_restful import Resource
from models.team import Team
from schemas.team import TeamSchema


class TeamList(Resource):
    team_schema = TeamSchema()

    def get(self):
        teams = Team.query.all()

        return {"data": self.team_schema.dump(teams, many=True)}