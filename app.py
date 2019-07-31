from flask import Flask
from flask_restful import Api
from db import db
from ma import ma
# Seeding Data
from seeding_data import players, tournaments, squads
# Models
from models.player import Player
from models.tournament import Tournament
from models.squad import Squad
# Resources
from resources.players import PlayerList
from resources.tournaments import TournamentList
from resources.squads import SquadList


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


if __name__ == '__main__':
    app.run(port=5000, debug=True)
