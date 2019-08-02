from flask import Flask
from flask_restful import Api
from db import db
from ma import ma
from flask_cors import CORS
# Seeding Data
from seeding_data import players, tournaments, squads, stages, teams, matches, goals, standings, stats, stat_rankings
# Models
from models.player import Player
from models.stage import Stage
from models.tournament import Tournament
from models.squad import Squad
from models.team import Team
from models.match import Match
from models.goal import Goal
from models.standing import Standing
from models.stat import Stat
from models.stat_ranking import StatRanking
# Resources
from resources.players import PlayerList
from resources.tournaments import TournamentList
from resources.squads import SquadList
from resources.stages import StageList
from resources.teams import TeamList
from resources.matches import MatchList
from resources.goals import GoalList
from resources.standings import StandingList
from resources.stats import StatList
from resources.stat_rankings import StatRankingList 

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['JSON_SORT_KEYS'] = False
app.secret_key = 'sdkjlsajdkslaj'  # app.config['JWT_SECRET_KEY']

api = Api(app)

db.init_app(app)
ma.init_app(app)

# Routes
api.add_resource(PlayerList, '/players')
api.add_resource(TournamentList, '/tournaments')
api.add_resource(SquadList, '/squads')
api.add_resource(StageList, '/stages')
api.add_resource(TeamList, '/teams')
api.add_resource(MatchList, '/matches')
api.add_resource(GoalList, '/goals')
api.add_resource(StandingList, '/standings')
api.add_resource(StatList, '/stats')
api.add_resource(StatRankingList, '/statrankings')


@app.before_first_request
def create_tables():
    db.create_all()


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, app=app, Player=Player)


@app.cli.command('seed')
def seed_all():
    db.create_all()
    # Players
    for player in players:
        new_player = Player(**player)
        db.session.add(new_player)
        db.session.commit()

    # Torunaments
    for tournament in tournaments:
        new_tournament = Tournament(**tournament)
        db.session.add(new_tournament)
        db.session.commit()

    # squads
    for squad in squads:
        new_squad = Squad(**squad)
        db.session.add(new_squad)
        db.session.commit()

    # stages
    for single_round in stages:
        new_round = Stage(**single_round)
        db.session.add(new_round)
        db.session.commit()

    # teams
    for team in teams:
        new_team = Team(**team)
        db.session.add(new_team)
        db.session.commit()

    # matches
    for match in matches:
        new_match = Match(**match)
        db.session.add(new_match)
        db.session.commit()

    # scorers
    for goal in goals:
        new_goal = Goal(**goal)
        db.session.add(new_goal)
        db.session.commit()

    # standings
    for standing in standings:
        new_standing = Standing(**standing)
        db.session.add(new_standing)
        db.session.commit()

    # stats
    for stat in stats:
        new_stat = Stat(**stat)
        db.session.add(new_stat)
        db.session.commit()

    # stat_rankings
    for sr in stat_rankings:
        new_sr = StatRanking(**sr)
        db.session.add(new_sr)
        db.session.commit()


if __name__ == '__main__':
    app.run(port=5000, debug=True)
