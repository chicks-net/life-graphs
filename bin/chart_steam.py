#!/usr/bin/env python

import os
import sys
import json

from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

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
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    game_id = Column(Integer, ForeignKey('game.id'))
    game = relationship(Game)
#    person_id = Column(Integer, ForeignKey('person.id'))
#    street_name = Column(String(250))
#    street_number = Column(String(250))
#    post_code = Column(String(250), nullable=False)

# check STATS_DIR
stats_dir = os.environ['STATS_DIR']
if not os.path.isdir(stats_dir):
	raise NoStatsDir

print stats_dir, "exists"
 
# Create an engine that stores data in the local directory's
# sqlalchemy_example.db file.
sqlite_file = stats_dir
sqlite_file += '/steam_games.db'

if not os.path.isfile(sqlite_file):
	sqlite_file = 'sqlite:///' + sqlite_file
	print 'creating', sqlite_file
	engine = create_engine(sqlite_file)

	# Create all tables in the engine. This is equivalent to "Create Table"
	# statements in raw SQL.
	Base.metadata.create_all(engine)
else:
	print sqlite_file, 'already exists, opening...'
	sqlite_file = 'sqlite:///' + sqlite_file
	engine = create_engine(sqlite_file)
	Base.metadata.bind = engine


# create session
DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()

# test insert
#test_game = Game(name="foo")
#session.add(test_game)
#session.commit()

# clear games table
session.query(Game).all()
cleared_games = session.query(Game).delete()
session.commit()

# read JSON into DB
steam_games = stats_dir + '/steam_games.json'
with open(steam_games, 'r') as content_file:
    games_content = content_file.read()
games = json.loads(games_content)

for g in games:
	#print g
	#print games[g]['name'], games[g]['app_id']
	insert_game = Game( **games[g] )
	session.add(insert_game)
	session.commit()

print "laaded games JSON"

# test read
session.query(Game).all()
#game = session.query(Game).first()
#print game.name
game_rows = session.query(Game).count()
print 'got', game_rows, 'games'
