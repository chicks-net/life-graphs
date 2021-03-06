#!/usr/bin/env python

import os
import sys
import json

from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

from datetime import datetime
#from pylab import *
import matplotlib.pyplot as plt
import matplotlib

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
	when = Column(DateTime, nullable=False)
	#level = Column(Integer)
	game_count = Column(Integer)
	achievement_count = Column(Integer)
	badge_count = Column(Integer)
	completion_rate = Column(Integer)
	game_card_count = Column(Integer)
	guide_count = Column(Integer)
	perfect_game_count = Column(Integer)
	review_count = Column(Integer)
	screenshot_count = Column(Integer)

# check STATS_DIR
stats_dir = os.environ['STATS_DIR']
if not os.path.isdir(stats_dir):
	print 'ERROR: please define valid directory in $STATS_DIR.'
	raise

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
	#print t, stats[t]['Games']
	when_obj = datetime.strptime(t, '%Y-%m-%d %H:%M')

#    completion_rate = Column(Integer)
#      "Avg. Game Completion Rate" : "40%",
	stats_rec = {
		'when': when_obj,
		'game_count': stats[t]['Games'],
		'achievement_count': stats[t]['Achievements'],
		'badge_count': stats[t].get('Badges Earned', 0),
		'game_card_count': stats[t].get('Game Cards', 0),
		'guide_count': stats[t].get('Guides', 0),
		'perfect_game_count': stats[t]['Perfect Games'],
		'review_count': stats[t]['Reviews'],
		'screenshot_count': stats[t]['Screenshots']}
	insert_stats = SteamProfile( **stats_rec )
	session.add(insert_stats)
	session.commit()

# count loaded stats
session.query(SteamProfile).all()
stats_rows = session.query(SteamProfile).count()
print 'loaded', stats_rows, 'stats rows'

whens = []
game_counts = []
guide_counts = []
screenshot_counts = []
perfect_game_counts = []
for stats in session.query(SteamProfile).order_by(SteamProfile.when):
	#print stats.when, stats.game_count
	#print stats
	whens.append(stats.when)
	game_counts.append(stats.game_count)
	perfect_game_counts.append(stats.perfect_game_count)
	guide_counts.append(stats.guide_count)

# matplotlib defaults
matplotlib.rcParams.update({'font.size': 10})
plt.figure(num=None, figsize=(8.5, 3), dpi=100)

# make a new chart
plt.xlabel('days')
fig = plt.figure(1)

ax1 = fig.add_subplot(221)
ax1.plot(whens, game_counts, color='b', label="Games")

ax2 = ax1.twinx()
ax2.plot(whens, perfect_game_counts, color='r', label="Perfect")
ax2.grid(ls='--', color='black')

h1, l1 = ax1.get_legend_handles_labels()
h2, l2 = ax2.get_legend_handles_labels()
ax1.legend(h1+h2, l1+l2, loc=2)

png_filename = 'Dash/steam_games.png'
plt.savefig(png_filename)

# check output size
png_stat = os.stat(png_filename)
print 'wrote', png_filename, ' (' + `png_stat.st_size`, 'bytes)'

print "END"
