from flask_restful import Resource
from models.stat import Stat
from models.squad import Squad
from models.player import Player
from schemas.stat import StatSchema
from flask import request
from sqlalchemy import func
from db import db

class StatList(Resource):
    stat_schema = StatSchema()

    def get(self):
        stat_type = request.args.get('type')
        sum_column = Squad.appearances

        if stat_type == 'goals':
            sum_column = Squad.goals        
        
        results = db.session.query(Squad.playerId, Player.firstName, Player.lastName, func.sum(sum_column).label('value')) \
            .join(Player, Player.id == Squad.playerId) \
            .order_by(func.sum(sum_column).desc()) \
            .group_by(Squad.playerId) \
            .limit(20) \
            .all()

        dict_res = [r._asdict() for r in results if r['value'] > 0]
        calculate_position(dict_res)
        return {"data": dict_res}


def calculate_position(stats):
    for i in range(len(stats)):
        if i > 0 and stats[i-1]['value'] == stats[i]['value']:
            stats[i]['position'] = stats[i-1]['position']
        else:
            stats[i]['position'] = i+1