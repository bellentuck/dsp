#The football.csv file contains the results from the English Premier League. 
# The columns labeled 'Goals' and 'Goals Allowed' contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in 'for' and 'against' goals.

# The below skeleton is optional.  You can use it or you can write the script with an approach of your choice.

import numpy as np


class Football(object):

    def __init__(self, data):
        f = open(data, 'r')
        lines = f.readlines()[1:]
        stripped = [line.strip('\n') for line in lines]
        parsed = [line.split(',') for line in stripped]
        self.parsed_array = np.asarray(parsed)
        f.close()

    def get_min_score_difference(self):
        return min([abs(int(line[5]) - int(line[6]))
                   for line in self.parsed_array])

    def get_team(self, index_value):
        for line in self.parsed_array:
            if abs(int(line[5]) - int(line[6])) == index_value:
                return line[0]

epl = Football('/Users/Ben/ds/metis/prework/dsp/python/football.csv')
print Football.get_team(epl, Football.get_min_score_difference(epl))



"""This whole operation can also be completed far more succinctly using `pandas`."""

import pandas as pd

epl = pd.read_csv('/Users/Ben/ds/metis/prework/dsp/python/football.csv')
goal_diffs = abs(epl['Goals']-epl['Goals Allowed'])
epl.ix[list(goal_diffs).index(min(goal_diffs))]['Team']

# Ain't pandas wonderful :)