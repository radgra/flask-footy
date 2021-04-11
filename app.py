from flask import Flask
from flask_restful import Api
from db import db
from ma import ma
from flask_cors import CORS
# Seeding Data
# Models
from models.player import Player
from models.stage import Stage
from models.tournament import Tournament
from models.squad import Squad
from models.team import Team
from models.match import Match
from models.goal import Goal
from models.standing import Standing
# Resources
from resources.players import PlayerList
from resources.tournaments import TournamentList
from resources.squads import SquadList
from resources.stages import StageList
from resources.teams import TeamList
from resources.matches import MatchList
from resources.goals import GoalList
from resources.standings import StandingList
import pdb
from datetime import datetime
import json


app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['JSON_SORT_KEYS'] = False
app.secret_key = 'sdkjlsajdkslaj'

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
    players = None
    with open('seed_data/players.json') as f:
        players = json.load(f)

    for player in players:
        new_player = Player(**player)
        db.session.add(new_player)
        db.session.commit()

    # Torunaments
    tournaments = None
    with open('seed_data/tournaments.json') as f:
        tournaments = json.load(f)

    for tournament in tournaments:
        new_tournament = Tournament(**tournament)
        db.session.add(new_tournament)
        db.session.commit()

    # stages
    stages = None
    with open('seed_data/stages.json') as f:
        stages = json.load(f)
        
    for single_round in stages:
        new_round = Stage(**single_round)
        db.session.add(new_round)
        db.session.commit()

    # teams
    teams = None
    with open('seed_data/teams.json') as f:
        teams = json.load(f)
    for team in teams:
        new_team = Team(**team)
        db.session.add(new_team)
        db.session.commit()



    tournament_data = None
    with open('seed_data/tournament_data.json') as f:
        tournament_data = json.load(f)
    for tournament in tournament_data:

        for squad_player in tournament['squad']:
            player = Player.query.filter(
                Player.lastName == squad_player['lastName'], Player.firstName == squad_player['firstName']).first()
            tournament_found = Tournament.query.filter_by(
                year=tournament['year']).first()
            new_squad_player = {"playerId": player.id, "tournamentId": tournament_found.id,
                                "goals": squad_player['goals'], "position": squad_player["position"], "appearances": squad_player['matches']}

            db.session.add(Squad(**new_squad_player))
            db.session.commit()

        # matches
        for match in tournament['matches']:
            home_team = Team.query.filter_by(name=match['homeTeam']).first()
            away_team = Team.query.filter_by(name=match['awayTeam']).first()
            tournament_found = Tournament.query.filter_by(
                year=tournament['year']).first()
            stage = Stage.query.filter(
                Stage.tournamentId == tournament_found.id, Stage.position == match['round']).first()
            match_date = datetime.strptime(
                match['date'].strip(), "%d.%m.%Y").date()
            match_obj = {"homeTeam": home_team, "awayTeam": away_team, "tournamentId": tournament_found.id, "stageId": stage.id,
                         "date": match_date, "goalsHomeTeam": match['result']['goalsHomeTeam'], "goalsAwayTeam": match['result']['goalsAwayTeam']}
            new_match = Match(**match_obj)
            db.session.add(new_match)
            db.session.commit()

            # homegoalscorers
            for goal in match['goalscorers']['homeGoalScorers']:
                if '(k)' in goal['player'] or '(s)' in goal['player']:
                    goal['player'] = goal['player'][3:]

                pl_split = goal['player'].split()
                found_player = Player.query.filter((Player.lastName == goal['player']) | (
                    (Player.lastName == pl_split[-1]) & (Player.firstName == pl_split[0]))).first()
                if not found_player:
                    pdb.set_trace()
                new_goal = Goal(matchId=new_match.id, minute=goal['minute'], playerId=found_player.id, homeTeamGoal=True)
                db.session.add(new_goal)
                db.session.commit()

            # awaygoalscorers
            for goal in match['goalscorers']['awayGoalScorers']:
                if '(k)' in goal['player'] or '(s)' in goal['player']:
                    goal['player'] = goal['player'][3:]

                pl_split = goal['player'].split()
                found_player = Player.query.filter((Player.lastName == goal['player']) | (
                    (Player.lastName == pl_split[-1]) & (Player.firstName == pl_split[0]))).first()
                if not found_player:
                    pdb.set_trace()
                new_goal = Goal(
                    matchId=new_match.id, minute=goal['minute'], playerId=found_player.id, awayTeamGoal=True)
                db.session.add(new_goal)
                db.session.commit()

        # standings
        for standing in tournament['standings']:

            found_team = Team.query.filter_by(
                name=standing['teamName']).first()

            tournament_found = Tournament.query.filter_by(
                year=tournament['year']).first()
            stage = Stage.query.filter(
                Stage.tournamentId == tournament_found.id, Stage.position == standing['round']).first()

            if not found_team:
                    pdb.set_trace()
            new_standing = Standing(stageId=stage.id, teamId=found_team.id,
                                    tournamentId=tournament_found.id, position=standing['position'], points=standing['points'], 
                                    wins=standing['position'], losses=standing['loses'], draws=standing['draws'],                                    
                                    goalsScored=standing['goalsScored'], goalsConceded=standing['goalsConceded'])
            db.session.add(new_standing)
            db.session.commit()



if __name__ == '__main__':
    app.run(port=5000, debug=True)
