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
import pdb

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
    import pickle
    file = open("data.pickle", "rb")
    data = pickle.load(file)
    # print(data['tournament_data'])

    db.create_all()
    # Players
    # tu powinienm wziac wszystkich graczy z zagranicy i z polski
    for player in data['players']:
        new_player = Player(**player)
        db.session.add(new_player)
        db.session.commit()

    # Torunaments
    for tournament in tournaments:
        new_tournament = Tournament(**tournament)
        db.session.add(new_tournament)
        db.session.commit()

    # for player in players:
    # 1.Refactoring rounds
    # stages
    for single_round in stages:
        new_round = Stage(**single_round)
        db.session.add(new_round)
        db.session.commit()

    # 2.Teams -> wziac wszystkie teamy i automatycznie flagi przypisac(pozniej), jak problem flag rozwiazalem ???
    # teams
    for team in data['teams']:
        new_team = Team(**team)
        db.session.add(new_team)
        db.session.commit()
    #     new_player = Player(**player)
    #     db.session.add(new_player)
    #     db.session.commit()

    for tournament in data['tournament_data']:
        # for squad in tournament['squad']:
        #     new_squad = Squad(**squad)
        #     db.session.add(new_squad)
        #     db.session.commit()
        # squads
        # 1)Player Id znalesc
        # 2)tournamentId
        # 3)appearances, position, goals
        for squad_player in tournament['squad']:
            # print("adsadwds")
            player = Player.query.filter(
                Player.lastName == squad_player['lastName'], Player.firstName == squad_player['firstName']).first()
            tournament_found = Tournament.query.filter_by(
                year=tournament['year']).first()
            new_squad_player = {"playerId": player.id, "tournamentId": tournament_found.id,
                                "goals": squad_player['goals'], "position": squad_player["position"], "appearances": squad_player['matches']}

            db.session.add(Squad(**new_squad_player))
            db.session.commit()

        # matches
        # 1) trzeba teams by foreign key
        # 2) trzeba tournament id by id
        # 3) round trzeba znalesc dla tournamenttu i position
        # 4) goals
        # Jak to zrobie to musze:
        # 5) dla kazdego matchu trzeba scorers
        # for match in matches:
        #     new_match = Match(**match)
        #     db.session.add(new_match)
        #     db.session.commit()
        for match in tournament['matches']:
            home_team = Team.query.filter_by(name=match['homeTeam']).first()
            away_team = Team.query.filter_by(name=match['awayTeam']).first()
            tournament_found = Tournament.query.filter_by(
                year=tournament['year']).first()
            stage = Stage.query.filter(
                Stage.tournamentId == tournament_found.id, Stage.position == match['round']).first()
            new_match = Match(homeTeam=home_team, awayTeam=away_team, tournamentId=tournament_found.id, stageId=stage.id,
                              date=match['date'], goalsHomeTeam=match['result']['goalsHomeTeam'], goalsAwayTeam=match['result']['goalsAwayTeam'])
            db.session.add(new_match)
            db.session.commit()

            # scorers
            for goal in match['goalscorers']['homeGoalScorers']:
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
