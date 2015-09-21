#!/usr/bin/env python


from __future__ import print_function

import os
import sys
import csv
import re

from datetime import datetime

# constants
steps_file = 'fitbit_activity.csv'

# functions
def recent_average(recent_list,count):
	recent_count = len(recent_list)
	if (recent_count < count):
		return 0

	average_items = recent_list[-count:-1]

	return sum(average_items)/count

def warning(*objs):
	print("WARNING: ", *objs, file=sys.stderr)

# get $STATS_DIR
env = os.environ
if 'STATS_DIR' in env:
	stats_dir = env['STATS_DIR']
else:
	raise OSError("no $STATS_DIR defined")

# open file
steps_file = stats_dir + '/' + steps_file
if os.path.isfile(steps_file):
	warning("reading " + steps_file)
else:
	raise OSError(steps_file + " is not a file")

recent_steps = []

with open(steps_file, 'rb') as steps_fh:
	step_read = csv.reader(steps_fh)
	headers = step_read.next()
	headers.append("steps_1wk")
	headers.append("steps_6wk")
	print(",".join(headers))

	for row in step_read:
		row_date = row[0]
		calories = row[1]
		steps = row[2]
		distance = row[3]
		floors = row[4]
		minutes_sedentary = row[5]
		minutes_lightly = row[6]
		minutes_fairly = row[7]
		minutes_very = row[8]
		calories_activity = row[9]

		row[0] = '"' + row_date + '"'

		commas = re.compile(',')
		steps = int(commas.sub('',steps))
		recent_steps.append(steps)
		row[2] = str(steps)

		calories = int(commas.sub('',calories))
		row[1] = str(calories)

		minutes_sedentary = int(commas.sub('',minutes_sedentary))
		row[5] = str(minutes_sedentary)

		minutes_lightly = int(commas.sub('',minutes_lightly))
		row[6] = str(minutes_lightly)

		minutes_fairly = int(commas.sub('',minutes_fairly))
		row[7] = str(minutes_fairly)

		minutes_very = int(commas.sub('',minutes_very))
		row[8] = str(minutes_very)

		calories_activity = int(commas.sub('',calories_activity))
		row[9] = str(calories_activity)

		steps_1wk = recent_average(recent_steps,7)
		row.append(str(steps_1wk))
		steps_6wk = recent_average(recent_steps,7*6)
		row.append(str(steps_6wk))

		#print row_date, steps, steps_1wk, steps_6wk
		print(','.join(row))

warning("END")
