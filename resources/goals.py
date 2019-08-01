from flask_restful import Resource
from models.goal import Goal
from schemas.goal import GoalSchema


class GoalList(Resource):
    goal_schema = GoalSchema()

    def get(self):
        goals = Goal.query.all()

        return {"data": self.goal_schema.dump(goals, many=True)}