import datetime

players = [
    {
        "born": datetime.datetime(2016, 10, 30),
        "lastName": "Mlynarczyk",
        "firstName": "Jozef"
    },
    {
        "born": datetime.datetime(2016, 10, 30),
        "lastName": "Dziuba",
        "firstName": "Marek"
    },
    {
        "born": datetime.datetime(2016, 10, 30),
        "lastName": "Kupcewicz",
        "firstName": "Janusz"
    },
]


tournaments = [
    {
        "title": "Niemcy 1938",
        "image": "assets/2006.jpg",
        "year": 1938
    },
    {
        "title": "Niemcy 1978",
        "image": "assets/1986.jpg",
        "year": 1974
    },
    {
        "title": "Argentyna 1978",
        "image": "assets/1986.jpg",
        "year": 1978
    },
    {
        "title": "Hiszpania 1982",
        "image": "assets/1982.jpg",
        "year": 1982
    },
    {
        "title": "Meksyk 1986",
        "image": "assets/1986.jpg",
        "year": 1986
    },
    {
        "title": "Korea i Japonia 2002",
        "image": "assets/2002.jpg",
        "year": 2002
    },
    {
        "title": "Niemcy 2006",
        "image": "assets/2006.jpg",
        "year": 2006
    },
    {
        "title": "Rosja 2018",
        "image": "assets/2006.jpg",
        "year": 2018
    },
]


squads = [
    {
        "playerId": 1,
        "tournamentId": 4,
        "appearances": 4,
        "goals": 3,
        "position": "Pomocnik",
    },
    {
        "playerId": 2,
        "tournamentId": 4,
        "appearances": 8,
        "goals": 1,
        "position": "Obronca",
    },
]


stages = [
    {
        "name": "Pierwsza Runda",
        "position": 1,
        "tournamentId":1
    },
    {
        "name": "Pierwsza Runda",
        "position": 1,
        "tournamentId":2
    },
    {
        "name": "Pierwsza Runda",
        "position": 2,
        "tournamentId":2
    },
    {
        "name": "Pierwsza Runda",
        "position": 3,
        "tournamentId":2
    },
    {
        "name": "Pierwsza Runda",
        "position": 4,
        "tournamentId":2
    },
    {
        "name": "Pierwsza Runda",
        "position": 1,
        "tournamentId":3
    },
    {
        "name": "Pierwsza Runda",
        "position": 2,
        "tournamentId":3
    },
    {
        "name": "Pierwsza Runda",
        "position": 3,
        "tournamentId":3
    },
    {
        "name": "Pierwsza Runda",
        "position": 4,
        "tournamentId":3
    },
    {
        "name": "Pierwsza Runda",
        "position": 1,
        "tournamentId":4
    },
    {
        "name": "Pierwsza Runda",
        "position": 2,
        "tournamentId":4
    },
    {
        "name": "Pierwsza Runda",
        "position": 3,
        "tournamentId":4
    },
    {
        "name": "Pierwsza Runda",
        "position": 4,
        "tournamentId":4
    },
    {
        "name": "Pierwsza Runda",
        "position": 1,
        "tournamentId":5
    },
    {
        "name": "Pierwsza Runda",
        "position": 2,
        "tournamentId":5
    },
    {
        "name": "Pierwsza Runda",
        "position": 1,
        "tournamentId":6
    },
    {
        "name": "Pierwsza Runda",
        "position": 1,
        "tournamentId":7
    },

]

teams = [
    {
        "flag": "/assets/flags/pl.svg",
        "name": "Polska"
    },
    {
        "flag": "/assets/flags/cm.svg",
        "name": "Kamerun"
    },
    {
        "flag": "/assets/flags/it.svg",
        "name": "Wlochy"
    },
    {
        "flag": "/assets/flags/pe.svg",
        "name": "Peru"
    },
    {
        "flag": "/assets/flags/be.svg",
        "name": "Belgia"
    },
]


matches = [
    {
        "homeTeamId": 1,
        "awayTeamId": 2,
        "tournamentId": 4,
        "date": datetime.datetime(2016, 10, 30),
        "goalsHomeTeam": 2,
        "goalsAwayTeam": 1,
        "stageId":1
    },
    {
        "homeTeamId": 1,
        "awayTeamId": 3,
        "tournamentId": 4,
        "date": datetime.datetime(2016, 10, 30),
        "goalsHomeTeam": 0,
        "goalsAwayTeam": 5,
        "stageId":1
    },
    {
        "homeTeamId": 1,
        "awayTeamId": 3,
        "tournamentId": 4,
        "date": datetime.datetime(2016, 10, 30),
        "goalsHomeTeam": 0,
        "goalsAwayTeam": 5,
        "stageId":2
    },
    {
        "homeTeamId": 1,
        "awayTeamId": 3,
        "tournamentId": 1,
        "date": datetime.datetime(2016, 10, 30),
        "goalsHomeTeam": 0,
        "goalsAwayTeam": 5,
        "stageId":1
    },
]

# Jak bede chcial pocwiczyc to moge walidacje zrobic pozniej
goals = [
    {
        "matchId": 1,
        "playerId": 2,
        "minute": 66,
        "homeTeamGoal": True,
    },
    {
        "matchId": 1,
        "playerId": 3,
        "minute": 13,
        "homeTeamGoal": True,
    },
    {
        "matchId": 1,
        "playerId": 3,
        "minute": 12,
        "awayTeamGoal": True,
    },
]


standings = [
    {
        "tournamentId": 4,
        "teamId": 1,
        "stageId": 1,
        "position": 1,
        "goalsScored": 8,
        "goalsConceded": 4,
        "points": 10
    },
    {
        "tournamentId": 4,
        "teamId": 2,
        "stageId": 1,
        "position": 2,
        "goalsScored": 4,
        "goalsConceded": 4,
        "points": 5
    },
]


stats = [
    {
        "playerId":1,
        "goals":10,
        "matches":30
    },
    {
        "playerId":2,
        "goals":20,
        "matches":40
    },
]

stat_rankings = [
    {
        "statId":1,
        "position":1,
        "rankingType":"goals"
    },
    {
        "statId":1,
        "position":1,
        "rankingType":"matchest"
    },
]