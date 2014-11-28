import os
import numpy as np

cor_data = np.genfromtxt('leagues_NBA_2014_team.csv', delimiter=',', skip_header=1,usecols=0)

print(cor_data)
