from flask import Flask
from flask_restful import Api
from db import db
from ma import ma
# Seeding Data
from seeding_data import players, tournaments, squads, rounds, teams
# Models
from models.player import Player
from models.round import Round
from models.tournament import Tournament
from models.squad import Squad
from models.team import Team
# Resources
from resources.players import PlayerList
from resources.tournaments import TournamentList
from resources.squads import SquadList
from resources.rounds import RoundList
from resources.teams import TeamList


app = Flask(__name__)
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
api.add_resource(RoundList, '/rounds')
api.add_resource(TeamList, '/teams')


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

    # rounds
    for single_round in rounds:
        new_round = Round(**single_round)
        db.session.add(new_round)
        db.session.commit()

    # teams
    for team in teams:
        new_team = Team(**team)
        db.session.add(new_team)
        db.session.commit()


if __name__ == '__main__':
    app.run(port=5000, debug=True)
