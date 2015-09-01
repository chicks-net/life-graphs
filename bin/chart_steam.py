#!/usr/bin/env python

import os
import sys
import json

from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

from pylab import *

#
# sqlalchemy classes
#
 
Base = declarative_base()
 
class Game(Base):
    __tablename__ = 'game'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    name_short = Column(String(250))
    app_id = Column(Integer)
    achievements = Column(Boolean)
    stats = Column(Boolean)
    leaderboards = Column(Boolean)
    global_achievements = Column(Boolean)
    global_leaderboards = Column(Boolean)
    url_achievements = Column(String(250))
    url_logo = Column(String(250))
    url_store = Column(String(250))
 
class GameStats(Base):
    __tablename__ = 'game_stats'
    id = Column(Integer, primary_key=True)
    game_id = Column(Integer, ForeignKey('game.id'))
    game = relationship(Game)

class SteamProfile(Base):
    __tablename__ = 'steam_profile'
    id = Column(Integer, primary_key=True)
    #when = Column(DateTime)
    when = Column(String(50), nullable=False)
    #level = Column(Integer)
    game_count = Column(Integer)

# check STATS_DIR
stats_dir = os.environ['STATS_DIR']
if not os.path.isdir(stats_dir):
	raise NoStatsDir

print stats_dir, "exists"
 
# Create an engine that stores data in the $STATS_DIR
sqlite_file = stats_dir
sqlite_file += '/steam_games.db'

if not os.path.isfile(sqlite_file):
	sqlite_file = 'sqlite:///' + sqlite_file
	print 'creating', sqlite_file
	engine = create_engine(sqlite_file)

	# Create all tables in the engine. This is equivalent
	# to "Create Table" statements in raw SQL.
	Base.metadata.create_all(engine)
else:
	print sqlite_file, 'already exists, opening...'
	sqlite_file = 'sqlite:///' + sqlite_file
	engine = create_engine(sqlite_file)


# create session
Base.metadata.bind = engine
DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()

# clear games table
session.query(Game).all()
cleared_games = session.query(Game).delete()
session.commit()

# read games JSON into DB
steam_games = stats_dir + '/steam_games.json'
with open(steam_games, 'r') as content_file:
    games_content = content_file.read()
games = json.loads(games_content)

for g in games:
	insert_game = Game( **games[g] )
	session.add(insert_game)
	session.commit()

# count games loaded
session.query(Game).all()
game_rows = session.query(Game).count()
print 'loaded', game_rows, 'games'

# clear stats table
session.query(SteamProfile).all()
cleared_stats = session.query(SteamProfile).delete()
session.commit()

# read game stats JSON into DB
steam_stats = stats_dir + '/steam.json'
with open(steam_stats, 'r') as content_file:
    stats_content = content_file.read()
stats = json.loads(stats_content)

for t in stats:
	stats_rec = {'when': t, 'game_count': stats[t]['Games']}
	insert_stats = SteamProfile( **stats_rec )
	session.add(insert_stats)
	session.commit()

# count loaded stats
session.query(SteamProfile).all()
stats_rows = session.query(SteamProfile).count()
print 'loaded', stats_rows, 'stats rows'

